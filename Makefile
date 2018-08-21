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

release:
	git checkout master && git pull
	git diff-index --quiet HEAD
	VERSION=$(python setup.py --version); \
	TAG_NAME=v${VERSION}; \
	twine upload dist/fraise-${VERSION}*; \
	git tag -a ${TAG_NAME}; \
	git push origin ${TAG_NAME}
