format:
	black .
	isort .

format-check:
	black . --check 
	isort . --check-only

typecheck:
	mypy --no-incremental

test:
	pytest --cov=src/ -v
