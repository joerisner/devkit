.DEFAULT_GOAL=help
.PHONY: build clean help setup

build: ## Build the package
	@uv build

clean: ## Remove temporary artifacts
	rm -rf ./dist
	rm -rf ./.ruff_cache

help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; \
	printf "\nUsage:\n\033[35m\033[0m"} /^[$$()% a-zA-Z_-]+:.*?##/ { \
	printf "  \033[35m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { \
	printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

setup: ## Setup the project
	@bin/setup
