BIN = $(VIRTUAL_ENV)/bin


.PHONY: test
test:
	$(BIN)/pytest

.PHONY: test_watch
test_watch:
	$(BIN)/ptw -- --last-failed --new-first  

.PHONY: test_coverage
test_coverage:
	$(BIN)/pytest --cov=app  --cov-report term

.PHONY: test_unit
test_unit:
	$(BIN)/pytest -m unit

.PHONY: test_integration
test_integration:
	$(BIN)/pytest -m integration