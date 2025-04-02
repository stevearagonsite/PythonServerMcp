# ============================================================================
# MCP Server Makefile
# ============================================================================

# Default target
.DEFAULT_GOAL := help

# ============================================================================
# HELP
# ============================================================================
help:
	@echo "============================================================================"
	@echo "MCP Server - Available Targets"
	@echo "============================================================================"
	@echo ""
	@echo "Setup:"
	@echo "  install              - Add a new dependency interactively"
	@echo "  install-dev          - Add a new dev dependency interactively"
	@echo "  install-deps         - Install all dependencies using uv"
	@echo "  upgrade-deps         - Upgrade all outdated dependencies"
	@echo "  hook-install         - Install git hooks"
	@echo ""
	@echo "Development:"
	@echo "  format               - Run black formatter"
	@echo "  lint                 - Run ruff linter with auto-fix"
	@echo "  clean                - Remove build artifacts and cache directories"
	@echo ""
	@echo "Server:"
	@echo "  run                  - Run the MCP server"
	@echo "  dev-server           - Run the MCP server in development mode"
	@echo "  stop-server          - Stop running MCP server and Inspector"
	@echo "  inspector            - Start MCP Inspector for testing"
	@echo ""
	@echo "Utilities:"
	@echo "  tree                 - Display project file structure"
	@echo "  help                 - Show this help message"
	@echo "============================================================================"

# ============================================================================
# SETUP TARGETS
# ============================================================================
install:
	@echo "Please enter dependency name:"
	@read DEP_NAME; \
	uv add $$DEP_NAME

install-dev:
	@echo "Please enter dev-dependency name:"
	@read DEP_NAME; \
	uv add $$DEP_NAME --optional dev

install-deps:
	@echo "Installing dependencies with uv..."
	@uv sync

upgrade-deps:
	@echo "Upgrading all outdated dependencies..."
	@uv lock --upgrade
	@uv sync
	@echo "Dependencies upgraded successfully!"

hook-install:
	@echo "Installing git hooks..."
	@mkdir -p .git/hooks
	@cp -f hooks/pre-commit .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
	@chmod +x .git/hooks/commit-msg
	@echo "Git hooks installed successfully!"

# ============================================================================
# DEVELOPMENT TARGETS
# ============================================================================
format:
	@echo "Running formatter with uv..."
	@uv run black .

lint:
	@echo "Running linter with uv..."
	@uv run ruff check --fix .

clean:
	@echo "Cleaning build artifacts..."
	@rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .ruff_cache/ __pycache__/ 
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "Build artifacts cleaned successfully!"

# ============================================================================
# SERVER TARGETS
# ============================================================================
run:
	@echo "Starting MCP server with uv..."
	@uv run python -m main

dev-server:
	@echo "Starting MCP server in development mode..."
	@uv run mcp dev src/mcp_server.py:server -e .

stop-server:
	@echo "Stopping MCP server and Inspector..."
	@-pkill -f "mcp dev" 2>/dev/null || true
	@-pkill -f "node.*modelcontextprotocol/inspector" 2>/dev/null || true
	@echo "Server stopped successfully."

# ============================================================================
# UTILITY TARGETS
# ============================================================================
tree:
	@echo "Displaying project file structure..."
	@tree -P "*.py|*.html|*.json" --prune -I "venv|temp|idx|ignore|ipynb_checkpoints|output|__pycache__"

inspector:
	@echo "Starting MCP Inspector for testing..."
	@npx @modelcontextprotocol/inspector uv run python -m main
