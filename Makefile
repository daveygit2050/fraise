.EXPORT_ALL_VARIABLES:

version = $(shell python setup.py --version)

init:
	pip install pipenv --upgrade
	pipenv install --dev

clean:
	rm -rf build
	rm -rf dist
	rm -rf fraise.egg-info

test:
	pipenv run py.test

build: clean test
	pipenv run python setup.py sdist bdist_wheel

release: build
	@echo "Version: $$version"
	pipenv run twine upload dist/fraise-${version}*
	git tag -a v$$version -m v$$version
	git push --tags
