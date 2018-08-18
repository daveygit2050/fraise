init:
	pipenv install
	pipenv shell
	export PYTHONPATH=${PYTHONPATH}:${PWD}

test:
	py.test tests

.PHONY: init test
