.EXPORT_ALL_VARIABLES:

version = $(shell python setup.py --version)

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

release: build
	@echo "Version: $$version"
	twine upload dist/fraise-${version}*
	git tag -a v$$version -m v$$version
	git push --tags
