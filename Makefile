
install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish: # publish wo add to PyPi
	poetry publish --dry-run
package-install: #install from OS
	python3 -m pip install --user dist/*.whl
lint: #flake8 brain_games dir
	poetry run flake8 brain_games
