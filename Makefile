# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
.EXPORT_ALL_VARIABLES:

# DOCKER TASKS
# Build the container
build: ## Build the container
	docker build -f Dockerfile -t aherrington-plangrid-homework .

build-test: ## Build the test container
	docker build -f Test-Dockerfile -t aherrington-plangrid-homework-test .

test: build-test ## Build the test container
	docker run -it aherrington-plangrid-homework-test

run: build ## Build the test container
	docker run -it -p 8000:8000 aherrington-plangrid-homework

run-debug: build ## Build the test container
	docker run -it -p 8000:8000 --env LOGLEVEL=DEBUG aherrington-plangrid-homework