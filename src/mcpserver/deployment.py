from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo_server")

@mcp.tool()
def add (a: int, b: int):
    """Add two numbers """
    return a + b