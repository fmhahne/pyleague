format:
	isort pyleague/*.py tests/*.py
	black .

check:
	pytest --cov-report term-missing --cov=pyleague -vv
	pylint pyleague
	mypy -p pyleague
