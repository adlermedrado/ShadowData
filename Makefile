help:
	@echo "targets:"
	@echo "test: Run all tests"
	@echo "coverage: Run tests"
	@echo "help: Show this help"

test:
	poetry run pytest -vvv

coverage:
	poetry run pytest -vvv --cov


.PHONY: test coverage 

