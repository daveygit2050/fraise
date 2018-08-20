init:
	pip install --user pipenv twine
	echo "PYTHONPATH=${PYTHONPATH}:${PWD}/fraise" > .env
	pipenv install --dev

test:
	pipenv run nosetests -v

build: test
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*
