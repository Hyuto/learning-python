clean:
	find . | grep -E '(__pycache__|\.pyc|\.lprof|\.pytest_cache|\.ipynb_checkpoints|\.mypy_cache)' | \
	xargs rm -rf

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

serve-doc:
	poetry run mkdocs serve

build-doc:
	poetry run mkdocs build
