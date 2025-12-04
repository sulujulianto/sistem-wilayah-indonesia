PYTHON ?= $(if $(wildcard .venv/bin/python3),.venv/bin/python3,python3)
UVICORN ?= $(PYTHON) -m uvicorn
APP_MODULE ?= app.main:app
HOST ?= 127.0.0.1
PORT ?= 8000

.PHONY: dev test lint type check smoke

dev:
	$(UVICORN) $(APP_MODULE) --host $(HOST) --port $(PORT) --reload

test:
	$(PYTHON) -m pytest -q

lint:
	$(PYTHON) -m ruff check .

type:
	$(PYTHON) -m mypy app

check: test lint type

smoke:
	./scripts/smoke_test.sh
