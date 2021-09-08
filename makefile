PIP?=pip
PYTHON?=python 3.7
CHANGELOG?=CHANGELOG.md

init: 
	echo "ENVIRONMENT=STAGING\nOOTI_AUTH=youremail\nOOTI_PASSWORD=yourpassword\nPYTHONPATH=$(PWD)" > .env	
	pip install pipenv
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
	pytest tests/test_auth.py
	pytest tests/test_collaboration.py
	pytest tests/test_costs.py
	pytest tests/test_deliverables.py
	pytest tests/test_invoicing.py
	pytest tests/test_others.py
	pytest tests/test_settings.py
	pytest tests/test_time.py

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

.PHONY: venv stop test tests test-class test-method cover clean
