# Server Status Checker MCP Server

A Model Context Protocol (MCP) server written in Python that checks if a website or service is up or down by sending HTTP GET requests.

Built using the official **FastMCP** framework (from the Python `mcp` SDK) and Python 3.12.

---

## Features
- **FastMCP SDK**: Built on the official Model Context Protocol library.
- **Python 3.12**: Runs in a modern, optimized Python environment created with `uv`.
- **Advanced HTTP client**: Uses `httpx` for asynchronous requests, custom user-agent headers, and redirect following.
- **Detailed Output**: Reports status (🟢 UP / 🔴 DOWN), redirect resolution, response time (ms), and exact HTTP status codes.

---

## Setup & Virtual Environment

The project uses `uv` to manage the virtual environment and dependencies.

### 1. Initialize Virtual Environment (Python 3.12)
```bash
# Recreate virtual environment using Python 3.12
uv venv --python 3.12 --clear
```

### 2. Install Dependencies
```bash
# Install required packages (mcp, httpx, etc.)
uv pip install -r requirements.txt
```

---

## Testing Locally

You can test the core logic and integration using the test script:
```bash
.venv/bin/python test_server.py
```

---

## Client Configuration (Antigravity AI Client)

To add this server to your Antigravity AI client:

### 1. Open the configuration file
Open the config file in your preferred text editor:
```bash
nano ~/.gemini/config/mcp_config.json
```

### 2. Add the configuration
Add the following configuration block under the `mcpServers` section of the JSON. Replace `/path/to/your/project` with the actual absolute path where this repository is located on your machine:

```json
{
  "mcpServers": {
    "server-status-checker": {
      "command": "/path/to/your/project/.venv/bin/python",
      "args": [
        "/path/to/your/project/server.py"
      ]
    }
  }
}
```

If you already have other MCP servers configured, append it inside the `mcpServers` block:

```json
    "server-status-checker": {
      "command": "/path/to/your/project/.venv/bin/python",
      "args": [
        "/path/to/your/project/server.py"
      ]
    }
```

### 3. Restart the Client
Restart the client to enable the `check_server_status` tool.

---

## Client Configuration (Claude Desktop)

To use this server in Claude Desktop, add it to your configuration file:

### Configuration File Location
On macOS:
`~/Library/Application Support/Claude/claude_desktop_config.json`

### Add the Server
Add the following configuration block. Make sure to use the absolute path to the virtual environment's Python interpreter:

```json
{
  "mcpServers": {
    "server-status-checker": {
      "command": "/path/to/your/project/.venv/bin/python",
      "args": [
        "/path/to/your/project/server.py"
      ]
    }
  }
}
```

Restart Claude Desktop, and the `check_server_status` tool will be ready to use!
