test:
	TERM=unknown pytest --cov-report term-missing --cov=src/ tests/ -vv

format-check:
	black --check .

format:
	black .

typecheck:
	mypy -p src --no-incremental