# Makefile for project cleanup and maintenance.
# Use `make help` to see available commands.

# Set the default goal to 'help' so that running `make` without arguments shows the help message.
.DEFAULT_GOAL := help

# Declare targets that are not files. This prevents `make` from getting confused if a file
# with the same name as the target exists, and it improves performance.
.PHONY: help clean

# --- ANSI Color Codes for pretty output ---
YELLOW := \033[0;33m
GREEN  := \033[0;32m
RESET  := \033[0m

## ====================================================================================
## HELP
## ====================================================================================

help:
	@echo "Available commands:"
	@echo "  ${GREEN}make clean${RESET}      - Remove Python cache..."
	@echo "  ${GREEN}make help${RESET}        - Show this help message."

## ====================================================================================
## CLEANING
## ====================================================================================

clean:
	@echo "${YELLOW}Cleaning up...${RESET}"
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	
	rm -rf uv.lock
	rm -rf simple_auth_manager_passwords.json.generated
	rm -rf airflow.cfg
	rm -rf airflow.db
