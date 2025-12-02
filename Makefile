PYTHON ?= python
UVICORN ?= $(PYTHON) -m uvicorn
APP_MODULE ?= app.main:app
HOST ?= 127.0.0.1
PORT ?= 8000

.PHONY: dev test lint type check

dev:
	$(UVICORN) $(APP_MODULE) --host $(HOST) --port $(PORT) --reload

test:
	$(PYTHON) -m pytest -q

lint:
	ruff check .

type:
	mypy app

check: test lint type
