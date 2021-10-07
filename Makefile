export CONSUMER_KEY
export CONSUMER_SECRET
export ACCESS_KEY
export ACCESS_SECRET

CONFIG = .env.local
APP = twitterlib


default: install install-dev

all: install install-dev fmt-check flake8


h help:
	@grep '^[a-z]' Makefile


install:
	pip install --upgrade pip
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt


fmt:
	black .
	isort .
fmt-check:
	black . --diff --check
	isort . --diff --check-only

pylint:
	pylint $(APP) || pylint-exit $$?

flake8:
	flake8 $(APP) --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 $(APP) --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

lint: flake8 pylint


demo-timeline:
	source $(CONFIG) \
		&& cd $(APP) \
		&& python -u timeline.py 'MichaelCurrin'

demo-trends:
	source $(CONFIG) \
		&& cd $(APP) \
		&& python trends.py
