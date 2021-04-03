BIN = $(VIRTUAL_ENV)/bin


.PHONY: test
test:
	$(BIN)/pytest

.PHONY: test_staged
test_staged:
	$(BIN)/pytest --picked --suppress-no-test-exit-code

.PHONY: test_watch
test_watch:
	$(BIN)/ptw -- --new-first  

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

.PHONY: flake8
flake8:
	$(BIN)/flake8 --version
	$(BIN)/flake8 .