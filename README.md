# mcp-databricks
The Databricks MCP (Model Context Protocol).

## Features
Current implementation support the "Git Credentials" and "Repos" endpoint from the Databricks API.

## Usage

### Using pip

1. Install Python from your preferred distribution like [python.org](https://www.python.org/downloads/) or [anaconda.com](https://www.anaconda.com/download) or other
2. Clone the repository `git clone https://github.com/jaymeanchante/mcp-databricks`
3. (Optional) Create a Python virtual environment from your preferred tool and activate it
3. Install requirements `pip install fastmcp==2.12.5`
4. Add the server configuration in your MCP client:
```json
"servers": {
  "databricks": {
    "command": "/path/to/python",
    "args": ["/path/to/mcp-databricks/mcp_databricks.py"],
    "env": {
      "DATABRICKS_HOST": "",
      "DATABRICKS_TOKEN": "",
    },
  }
}
```

### Using uv
1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Clone the repository `git clone https://github.com/jaymeanchante/mcp-databricks`
3. Add the server configuration in your MCP client:
```json
"servers": {
  "databricks": {
    "command": "uvx",
    "args": ["--with", "fastmcp==2.12.5", "python", "/path/to/mcp-databricks/mcp_databricks.py"],
    "env": {
      "DATABRICKS_HOST": "",
      "DATABRICKS_TOKEN": "",
    },
  }
}
```

## Support
The MCP Databricks API currently support the following endpoints:

| Support | Type | Category | Subcategory |
|---------|------|----------|-------------|
|   ✅   | workspace | databricks_workspace | git_credentials |
|   ✅   | workspace | databricks_workspace | repos |
|   ✅   | workspace | databricks_workspace | secret |
|   ✅   | workspace | databricks_workspace | workspace |