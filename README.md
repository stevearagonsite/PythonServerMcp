# Python Server MCP - Cryptocurrency Price Service

This project implements an MCP (Model Context Protocol) server that provides cryptocurrency price information. The server is built using Python and the MCP framework to create an API that can be consumed by different clients.

## Features

- Real-time cryptocurrency price retrieval
- Environment-based configuration (development, production, staging, local)
- CoinMarketCap API integration
- Docker container deployment

## Requirements

- Python 3.12+
- uv (package and virtual environment manager)
- Docker (optional, for container execution)

## Installation

### Using uv (recommended)

```bash
# Clone the repository
git clone <repository-url>
cd PythonServerMcp
```

### Create and activate virtual environment with uv
```bash
uv venv
source .venv/bin/activate
```

# Install dependencies
`uv sync`

## Configuration

1. Create a `.env` file in the project root with the following variables:

```
ENVIRONMENT=DEV  # Options: LOCAL, DEV, STAGING, PROD
COINMARKETCAP_API_KEY=your_api_key_here
```

2. You can also create specific environment files for each environment:
   - `.dev.env` - For development environment
   - `.staging.env` - For staging environment
   - `.prod.env` - For production environment

## Usage

### Local Execution

```bash
python main.py
```

This will start the MCP server that will listen for requests through standard input/output (stdio).

### Using Docker

```bash
# Build the image
docker build -t test-mcp -f Dockerfile --platform linux/amd64 .

# Run the container
docker run -it test-mcp
```

## Project Structure

```
.
├── Dockerfile          # Docker configuration
├── main.py             # Application entry point
├── pyproject.toml      # Dependencies configuration
├── start.sh            # Docker startup script
└── src/                # Source code
    ├── __init__.py     # MCP server initialization
    └── core/           # Core modules
        ├── common/     # Shared schemas and models
        ├── config.py   # Application configuration
        ├── services/   # Application services
        ├── settings/   # Environment-specific settings
        └── utils/      # Utilities
```

## Development

### Adding New Tools to the MCP Server

To add a new tool to the MCP server, follow these steps:

1. Define the function in the `src/__init__.py` file
2. Register the tool in the `main()` function
3. Document the tool with docstrings

Example:

```python
@server.add_tool
def my_new_tool(parameter1: str, parameter2: int) -> str:
    """
    Description of what the tool does.
    
    Args:
        parameter1: Description of parameter 1
        parameter2: Description of parameter 2
        
    Returns:
        Description of what is returned
    """
    # Tool implementation
    return result
```
