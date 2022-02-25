format:
	isort pyleague/*.py tests/*.py
	black .

check:
	pytest --cov-report term-missing --cov=pyleague -vv
	pylint pyleague -d C0330,C0326
	mypy --no-strict-optional --ignore-missing-imports -p pyleague
