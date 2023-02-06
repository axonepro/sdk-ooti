PIP?=pip
PYTHON?=python 3.8.2
CHANGELOG?=CHANGELOG.md

env:
	@if [[ -f ".env" ]]; then\
		echo ".env file already exists.";\
	else\
		echo "ENVIRONMENT=STAGING\nOOTI_AUTH=youremail\nOOTI_PASSWORD=yourpassword\nPYTHONPATH=$(PWD)" > .env;\
	fi

init: env
	pip install pipenv
	pip install gitchangelog
	pipenv --$(PYTHON)
	pipenv install -r ./requirements/requirements.txt
	pipenv install -r ./requirements/dev-requirements.txt --dev
	pipenv shell

install:
	pipenv install

start:
	pipenv shell

test:
	pytest tests/$(filename).py

test-class:
	pytest tests/$(filename) -k "$(class)"

test-method:
	pytest tests/$(filename) -k "$(method)"

tests:
	pytest

pythonalias:
	echo '\npython="python3"\npip=pip3' >> ~/.zshrc

changelog:
	gitchangelog > $(CHANGELOG).tmp
	sed '/~/d' ./$(CHANGELOG).tmp > $(CHANGELOG)
	rm $(CHANGELOG).tmp

stop:
	$(shell exit)
clean:
	rm -Rf Pipfile Pipfile.lock
	rm -Rf $(shell pipenv --py | rev | cut -d'/' -f3- | rev)

deploy:
	python setup.py sdist bdist_wheel
	python -m twine check dist/*
	python -m twine upload --verbose -r pypi dist/*

.PHONY: venv stop test tests test-class test-method cover clean deploy first-deploy