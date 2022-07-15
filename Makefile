format:
	poetry run black .
	poetry run isort .

format-check:
	poetry run black . --check 
	poetry run isort . --check-only

typecheck:
	poetry run mypy src/ --no-incremental

test:
	poetry run pytest --cov=src/ -v
