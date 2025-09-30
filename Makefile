.PHONY: default help run update-inventory shopify-dev shopify-push git-pull shopify-pull

# Python executable (override: make PY=python3)
PY ?= python

# Path to the inventory updater (override: make UPDATE_SCRIPT=path/to/file)
UPDATE_SCRIPT ?= scripts/inventory/update.py

# Default target
default: update-inventory

# Show available commands
help:
	@echo "Available targets:"
	@echo "  make update-inventory - Run inventory updater ($(UPDATE_SCRIPT))"
	@echo "  make run              - Alias of update-inventory"
	@echo "  make shopify-dev   - Run Shopify theme dev (requires Shopify CLI)"
	@echo "  make shopify-push  - Push theme to store (requires Shopify CLI)"
	@echo "  make git-pull      - git pull from current branch"
	@echo "  make shopify-pull  - Pull theme from store (requires Shopify CLI)"

# Run the update script
run:
	$(PY) $(UPDATE_SCRIPT)

# Alias
update-inventory: run

# Shopify helpers (optional; set STORE env var)
shopify-dev:
	shopify theme dev --store syx10i-mq.myshopify.com

shopify-push:
	shopify theme push --store syx10i-mq.myshopify.com

# Pull latest repo changes
git-pull:
	git pull --ff-only

# Pull theme from the store (use STORE env var)
shopify-pull:
	shopify theme pull --store syx10i-mq.myshopify.com