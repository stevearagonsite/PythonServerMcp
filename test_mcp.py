# test_mcp.py
try:
    import mcp

    print(f"MCP package found: {mcp.__file__}")
    print(f"Available modules in mcp: {dir(mcp)}")
except ImportError as e:
    print(f"Error importing MCP: {e}")

try:
    from mcp.server import Server

    print("Successfully imported Server from mcp.server")
except ImportError as e:
    print(f"Error importing Server: {e}")

try:
    from mcp.tools import Tool

    print("Successfully imported Tool from mcp.tools")
except ImportError as e:
    print(f"Error importing Tool: {e}")

# Try alternative imports
try:
    from mcp.server.tool import Tool

    print("Successfully imported Tool from mcp.server.tool")
except ImportError as e:
    print(f"Error importing Tool from mcp.server.tool: {e}")

try:
    import importlib

    spec = importlib.util.find_spec("mcp.server")
    if spec:
        server_module = importlib.import_module("mcp.server")
        print(f"mcp.server module found: {server_module.__file__}")
        print(f"Available in mcp.server: {dir(server_module)}")
except Exception as e:
    print(f"Error inspecting mcp.server: {e}")
