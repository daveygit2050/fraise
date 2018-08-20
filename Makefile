init:
	pip install --user pipenv twine
	echo "PYTHONPATH=${PYTHONPATH}:${PWD}/fraise" > .env
	pipenv install --dev

clean:
	rm -rf build
	rm -rf dist

test:
	pipenv run nosetests -v

build: clean test
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*
