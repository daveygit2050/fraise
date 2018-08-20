init:
	pip install --user pipenv twine
	pipenv install --dev

test:
	pipenv run nosetests -v

build: test
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*
