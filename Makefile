export CONSUMER_KEY
export CONSUMER_SECRET
export ACCESS_KEY
export ACCESS_SECRET

export PYTHONPATH

CONFIG = .env.local
APP_DIR = twitterlib


default: install install-dev

all: install install-dev fmt-check lint typecheck


h help:
	@grep '^[a-z]' Makefile


install:
	pip install --upgrade pip
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt


upgrade:
	pip install pip --upgrade
	pip install -r requirements.txt --upgrade
	pip install -r requirements-dev.txt --upgrade


fmt:
	black .
	isort .

fmt-check:
	black . --diff --check
	isort . --diff --check-only

pylint:
	source .env \
		&& pylint $(APP_DIR) \
		|| pylint-exit $$?

flake8:
	flake8 . --select=E9,F63,F7,F82 --show-source
	flake8 . --exit-zero

lint: pylint flake8

fix: fmt lint


t typecheck:
	mypy $(APP_DIR)



demo-timeline:
	source $(CONFIG) \
		&& cd $(APP_DIR) \
		&& python -u timeline.py 'MichaelCurrin'

demo-trends:
	source $(CONFIG) \
		&& cd $(APP_DIR) \
		&& python trends.py
