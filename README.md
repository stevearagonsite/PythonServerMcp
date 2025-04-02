# Python Server MCP - Cryptocurrency Price Service

This project implements an MCP (Model Context Protocol) server that provides cryptocurrency price information. The server is built using Python and the MCP framework to create an API that can be consumed by different clients.

## Docker

Docker build:
`docker build -t mcp/python-server-mcp -f Dockerfile .`

Add the following to your `mcp.json` file:
```
{
  "mcpServers": {
    "python-server-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-p",
        "8000:8000",
        "-e",
        "ENVIRONMENT",
        "-e",
        "COINMARKETCAP_API_KEY",
        "mcp/python-server-mcp"
      ],
      "env": {
        "ENVIRONMENT": "PRODUCTION",
        "COINMARKETCAP_API_KEY": "your-api-key",
      }
    }
  }
}
```

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
├── main.py
└── src
    ├── __init__.py
    ├── core
    │   ├── common
    │   │   ├── crypto_schema.py
    │   │   └── schema.py
    │   ├── config.py
    │   ├── settings
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── development.py
    │   │   ├── environment.py
    │   │   ├── local.py
    │   │   ├── production.py
    │   │   └── staging.py
    │   └── utils
    │       ├── datetime.py
    │       ├── extended_enum.py
    │       ├── filename_generator.py
    │       ├── passwords.py
    │       ├── query_utils.py
    │       └── redis.py
    ├── mcp_server.py
    ├── resources
    │   ├── __init__.py
    │   └── coinmarketcap_resource.py
    ├── server.py
    ├── services
    │   ├── __init__.py
    │   └── coinmarketcap_service.py
    └── tools
        ├── __init__.py
        └── prices.py
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
