# MCP Deployment

Add the following server configuration under `mcpServers` in your MCP config file:

```json
{
  "mcpServers": {
    "MyFirstMCPServer": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/girish3349/MCP-Deployment.git",
        "mcp-server"
      ]
    }
  }
}
```

Steps:
1. Open your MCP configuration file.
2. Add or update the `mcpServers` section.
3. Save the file.
4. Start MCP so it can load the configured server definition.
