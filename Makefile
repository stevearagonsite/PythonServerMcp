# ============================================================================
# MCP Server Makefile
# ============================================================================

# Default target
.DEFAULT_GOAL := help

# Python interpreter and virtual environment
PYTHON := python
UV := uv

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
	@echo "  uninstall            - Remove a dependency interactively"
	@echo "  install-dev          - Add a new dev dependency interactively"
	@echo "  uninstall-dev        - Remove a dev dependency interactively"
	@echo "  install-deps         - Install all dependencies using uv"
	@echo "  upgrade-deps         - Upgrade all outdated dependencies"
	@echo "  hook-install         - Install git hooks"
	@echo "  claude-install       - Install MCP server in Claude Desktop"
	@echo "  claude-uninstall     - Uninstall MCP server from Claude Desktop"
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
	@echo "Docker:"
	@echo "  docker-build         - Build Docker image"
	@echo "  docker-run           - Run Docker container"
	@echo "  docker-stop          - Stop Docker container"
	@echo ""
	@echo "Documentation:"
	@echo "  docs                 - Generate API documentation"
	@echo "  serve-docs           - Serve documentation locally"
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

uninstall:
	@echo "Please enter dependency name:"
	@read DEP_NAME; \
	uv remove $$DEP_NAME

install-dev:
	@echo "Please enter dev-dependency name:"
	@read DEP_NAME; \
	uv add $$DEP_NAME --optional dev

uninstall-dev:
	@echo "Please enter dev-dependency name:"
	@read DEP_NAME; \
	uv remove $$DEP_NAME --optional dev

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

claude-install:
	@echo "Installing weather MCP server in Claude Desktop..."
	@uv run mcp install mcp_server.py:server --name weather -e .
	@echo "Weather MCP server installed in Claude Desktop. Please restart Claude to apply changes."

claude-uninstall:
	@echo "Uninstalling weather MCP server from Claude Desktop..."
	@CONFIG_DIR="$$HOME/Library/Application Support/Claude/claude_desktop_config.json" && \
	if [ -f "$$CONFIG_DIR" ]; then \
		echo "Updating Claude Desktop configuration..."; \
		TMP_FILE=$$(mktemp) && \
		jq 'if .mcpServers.weather then del(.mcpServers.weather) else . end' "$$CONFIG_DIR" > "$$TMP_FILE" && \
		mv "$$TMP_FILE" "$$CONFIG_DIR" && \
		echo "Weather MCP server removed from Claude Desktop. Please restart Claude to apply changes."; \
	else \
		echo "Claude Desktop configuration not found. Nothing to uninstall."; \
	fi

# ============================================================================
# DEVELOPMENT TARGETS
# ============================================================================
format:
	@echo "Running formatter with uv..."
	@$(UV) run black .

lint:
	@echo "Running linter with uv..."
	@$(UV) run ruff check --fix .


clean:
	@echo "Cleaning build artifacts..."
	@rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .ruff_cache/ __pycache__/ htmlcov/ .coverage
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "Build artifacts cleaned successfully!"

# ============================================================================
# SERVER TARGETS
# ============================================================================
run:
	@echo "Starting MCP server with uv..."
	@$(UV) run python -m main

dev-server:
	@echo "Starting MCP server in development mode..."
	@$(UV) run mcp dev src/mcp_server.py:server -e .

stop-server:
	@echo "Stopping MCP server and Inspector..."
	@-pkill -f "mcp dev" 2>/dev/null || true
	@-pkill -f "node.*modelcontextprotocol/inspector" 2>/dev/null || true
	@echo "Server stopped successfully."

# ============================================================================
# DOCKER TARGETS
# ============================================================================
docker-build:
	@echo "Building Docker image..."
	@docker build -t mcp/python-server-mcp -f Dockerfile .

docker-run:
	@echo "Running Docker container..."
	@docker run -d --name mcp-server -p 3000:3000 mcp/python-server-mcp

docker-stop:
	@echo "Stopping Docker container..."
	@docker stop mcp/python-server-mcp || true
	@docker rm mcp/python-server-mcp || true

# ============================================================================
# DOCUMENTATION TARGETS
# ============================================================================
docs:
	@echo "Generating API documentation..."
	@$(UV) run sphinx-build -b html docs/source docs/build
	@echo "Documentation generated in docs/build/"

serve-docs:
	@echo "Serving documentation locally..."
	@$(UV) run python -m http.server 8080 --directory docs/build

# ============================================================================
# UTILITY TARGETS
# ============================================================================
tree:
	@echo "Displaying project file structure..."
	@tree -P "*.py|*.html|*.json" --prune -I "venv|temp|idx|ignore|ipynb_checkpoints|output|__pycache__|.ruff_cache|.pytest_cache|htmlcov"

inspector:
	@echo "Starting MCP Inspector for testing..."
	@npx @modelcontextprotocol/inspector $(UV) run python -m main
