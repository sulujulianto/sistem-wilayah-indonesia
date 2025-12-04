#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-8000}"
BASE_URL="http://${HOST}:${PORT}"
SMOKE_START_SERVER="${SMOKE_START_SERVER:-1}"
ALLOW_ORIGINS="${ALLOW_ORIGINS:-}"
LOG_FILE="${SMOKE_LOG:-/tmp/swi_smoke.log}"

if [[ -x ".venv/bin/python3" ]]; then
  PYTHON=".venv/bin/python3"
else
  PYTHON="${PYTHON:-python3}"
fi

TMP_DIR="$(mktemp -d)"
SERVER_PID=""

cleanup() {
  if [[ -n "$SERVER_PID" ]] && ps -p "$SERVER_PID" >/dev/null 2>&1; then
    kill "$SERVER_PID" >/dev/null 2>&1 || true
  fi
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

start_server() {
  echo "Starting server at $BASE_URL ..."
  "$PYTHON" -m uvicorn app.main:app --host "$HOST" --port "$PORT" --log-level warning >"$LOG_FILE" 2>&1 &
  SERVER_PID=$!
}

wait_for_health() {
  for _ in {1..60}; do
    if curl -sSf "$BASE_URL/health" >/dev/null 2>&1; then
      echo "Server is healthy"
      return 0
    fi
    sleep 0.2
  done
  echo "Server did not become healthy in time" >&2
  if [[ -f "$LOG_FILE" ]]; then
    echo "Server log ($LOG_FILE):" >&2
    tail -n 20 "$LOG_FILE" >&2 || true
  fi
  exit 1
}

require_status() {
  local status="$1"
  local expected="$2"
  if [[ "$status" != "$expected" ]]; then
    echo "Unexpected status: got $status, expected $expected" >&2
    exit 1
  fi
}

require_in_list() {
  local status="$1"
  shift
  for exp in "$@"; do
    if [[ "$status" == "$exp" ]]; then
      return 0
    fi
  done
  echo "Unexpected status: got $status, expected one of: $*" >&2
  exit 1
}

if [[ "$SMOKE_START_SERVER" != "0" ]]; then
  start_server
fi

wait_for_health

echo "1) GET /health"
HEALTH_BODY="$(curl -sSf "$BASE_URL/health")"
BODY="$HEALTH_BODY" "$PYTHON" - <<'PY'
import json, os, sys
data = json.loads(os.environ["BODY"])
assert data.get("status") == "ok", f"unexpected health: {data}"
PY

echo "2) GET /v1/meta"
META_HEADERS="$TMP_DIR/meta_headers.txt"
META_BODY="$TMP_DIR/meta_body.json"
META_STATUS="$(curl -sS -w '%{http_code}' -D "$META_HEADERS" -o "$META_BODY" "$BASE_URL/v1/meta")"
require_status "$META_STATUS" "200"
ETAG="$(grep -i '^etag:' "$META_HEADERS" | tail -1 | awk '{print $2}' | tr -d '\r')"
if [[ -z "$ETAG" ]]; then
  echo "ETag not found on /v1/meta" >&2
  exit 1
fi
BODY="$(cat "$META_BODY")" "$PYTHON" - <<'PY'
import json, os, sys
data = json.loads(os.environ["BODY"])
required = {"dataset_name", "dataset_version", "last_updated", "coverage", "computed_coverage"}
missing = required - data.keys()
assert not missing, f"missing keys in /v1/meta: {missing}"
PY

echo "3) HEAD /v1/meta"
META_HEAD_STATUS="$(curl -sS -I -o /dev/null -w '%{http_code}' "$BASE_URL/v1/meta")"
require_status "$META_HEAD_STATUS" "200"

echo "4) GET /v1/meta with If-None-Match -> 304"
META_304_STATUS="$(curl -sS -H "If-None-Match: $ETAG" -o /dev/null -w '%{http_code}' "$BASE_URL/v1/meta")"
require_status "$META_304_STATUS" "304"

echo "5) HEAD /v1/provinces?limit=5&offset=0"
PROV_HEAD_STATUS="$(curl -sS -I -o /dev/null -w '%{http_code}' "$BASE_URL/v1/provinces?limit=5&offset=0")"
require_status "$PROV_HEAD_STATUS" "200"

echo "6) GET /v1/provinces?limit=5&offset=0"
PROV_BODY="$TMP_DIR/provinces_body.json"
PROV_STATUS="$(curl -sS -w '%{http_code}' -o "$PROV_BODY" "$BASE_URL/v1/provinces?limit=5&offset=0")"
require_status "$PROV_STATUS" "200"
BODY="$(cat "$PROV_BODY")" "$PYTHON" - <<'PY'
import json, os, sys
data = json.loads(os.environ["BODY"])
assert "count" in data and "items" in data, "count/items missing in provinces list"
items = data["items"]
assert isinstance(items, list), "items is not a list"
assert len(items) <= 5, "items length exceeds limit"
PY

echo "7) GET /v1/provinces/jabar"
JABAR_BODY="$(curl -sSf "$BASE_URL/v1/provinces/jabar")"
BODY="$JABAR_BODY" "$PYTHON" - <<'PY'
import json, os
data = json.loads(os.environ["BODY"])
assert data.get("name") == "Jawa Barat", f"Unexpected province name: {data.get('name')}"
PY

echo "8) GET /v1/search?q=bima&type=all"
SEARCH_BODY="$TMP_DIR/search_body.json"
SEARCH_STATUS="$(curl -sS -w '%{http_code}' -o "$SEARCH_BODY" "$BASE_URL/v1/search?q=bima&type=all")"
require_status "$SEARCH_STATUS" "200"
BODY="$(cat "$SEARCH_BODY")" "$PYTHON" - <<'PY'
import json, os
data = json.loads(os.environ["BODY"])
assert data.get("count", 0) >= 1, "Search returned no results"
PY

if [[ -n "$ALLOW_ORIGINS" ]]; then
  TEST_ORIGIN="$(echo "$ALLOW_ORIGINS" | cut -d',' -f1 | xargs)"
  echo "9) CORS check with Origin: $TEST_ORIGIN"
  CORS_HEADERS="$TMP_DIR/cors_headers.txt"
  CORS_STATUS="$(curl -sS -I -H "Origin: $TEST_ORIGIN" -o /dev/null -w '%{http_code}' "$BASE_URL/v1/meta")"
  require_in_list "$CORS_STATUS" "200" "304"
  ALLOW_HEADER="$(curl -sS -I -H "Origin: $TEST_ORIGIN" "$BASE_URL/v1/meta" | grep -i '^access-control-allow-origin:' | tail -1 | awk '{print $2}' | tr -d '\r')"
  if [[ "$ALLOW_HEADER" != "$TEST_ORIGIN" ]]; then
    echo "CORS header mismatch: expected $TEST_ORIGIN got ${ALLOW_HEADER:-<missing>}" >&2
    exit 1
  fi
else
  echo "9) CORS check skipped (ALLOW_ORIGINS empty)"
fi

echo "OK - semua smoke test lulus"
