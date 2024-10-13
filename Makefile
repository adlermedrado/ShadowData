help:
	@echo "targets:"
	@echo "test: Run all tests"
	@echo "coverage: Run tests"
	@echo "help: Show this help"

test:
	poetry run pytest -vvv

coverage:
	poetry run pytest -vvv --cov

format:
	poetry run ruff format .

check:
	poetry run ruff check .

check-fix:
	poetry run ruff check --fix .

.PHONY: test coverage 

