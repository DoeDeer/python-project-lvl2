PIP_USERNAME?=
PIP_PASSWORD?=


install:
	poetry install
lint:
	poetry run flake8 gendiff
publish:
	poetry publish --build \
	 --username $(shell echo ${PIP_USERNAME}) \
	 --password $(shell echo ${PIP_PASSWORD}) \
	  -r test-pypi

.PHONY: install lint publish
