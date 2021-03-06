BIN = $(VIRTUAL_ENV)/bin


.PHONY: test
test:
	$(BIN)/pytest

.PHONY: test_staged
test_staged:
	$(BIN)/pytest --picked --suppress-no-test-exit-code

.PHONY: test_watch_staged
test_watch_staged:
	$(BIN)/ptw -- --picked --suppress-no-test-exit-code

.PHONY: test_watch_unit
test_watch:
	$(BIN)/ptw -- --new-first -m unit

.PHONY: test_watch_integration
test_watch_integration:
	$(BIN)/ptw -- --new-first -m integration

.PHONY: test_coverage
test_coverage:
	$(BIN)/pytest --cov=app --cov-config=.coveragerc --cov-report term

.PHONY: test_unit
test_unit:
	$(BIN)/pytest -m unit

.PHONY: test_integration
test_integration:
	$(BIN)/pytest -m integration

.PHONY: black
black:
	$(BIN)/black --version
	$(BIN)/black .

.PHONY: black_check
black_check:
	$(BIN)/black --version
	$(BIN)/black --check .

.PHONY: flake8
flake8:
	$(BIN)/flake8 --version
	$(BIN)/flake8 .

.PHONY: isort
isort:
	$(BIN)/isort --version
	$(BIN)/isort .

.PHONY: isort_check
isort_check:
	$(BIN)/isort --version
	$(BIN)/isort --check .

.PHONY: serve
serve:
	$(BIN)/uvicorn app.main.server:app --reload