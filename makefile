PIP?=pip
PYTHON?=python 3.7
CHANGELOG?=CHANGELOG.md

init:
	echo "ENVIRONMENT=STAGING\nOOTI_AUTH=youremail\nOOTI_PASSWORD=yourpassword\nPYTHONPATH=$(PWD)" > .env
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
	pytest tests/test_annexe.py
	pytest tests/test_area.py
	pytest tests/test_bank.py
	pytest tests/test_celery_task.py
	pytest tests/test_client.py
	pytest tests/test_contact.py
	pytest tests/test_contract.py
	pytest tests/test_cost.py
	pytest tests/test_currency.py
	pytest tests/test_custom_field.py
	pytest tests/test_default.py
	pytest tests/test_email.py
	pytest tests/test_employee.py
	pytest tests/test_expense.py
	pytest tests/test_file.py
	pytest tests/test_goal.py
	pytest tests/test_inbound_email.py
	pytest tests/test_indicator.py
	pytest tests/test_invoice.py
	pytest tests/test_job.py
	pytest tests/test_milestone.py
	pytest tests/test_newsletter.py
	pytest tests/test_note.py
	pytest tests/test_notification.py
	pytest tests/test_orguser.py
	pytest tests/test_payment.py
	pytest tests/test_phase.py
	pytest tests/test_post.py
	pytest tests/test_profile.py
	pytest tests/test_project.py
	pytest tests/test_revision.py
	pytest tests/test_role.py
	pytest tests/test_tag.py
	pytest tests/test_task.py
	pytest tests/test_timeperiod.py
	pytest tests/test_trip.py

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
	python setup.py sdist bdist_whee
	python -m twine check dist/*
	python -m twine upload -r pypi dist/*

.PHONY: venv stop test tests test-class test-method cover clean deploy first-deploy