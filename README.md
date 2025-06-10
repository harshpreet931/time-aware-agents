# Time-Aware MCP Server

This project provides a Model Context Protocol (MCP) server designed to make AI agents time-aware. It currently features a simple tool to extract the time component from a date-time string.

## Features

- **Time Extraction Tool**: Extracts the time (e.g., "16:30:00") from an ISO 8601 date-time string (e.g., "2025-06-09T16:30:00Z").
- **MCP Compatible**: Built using the Python MCP SDK, allowing easy integration with MCP clients like Claude for Desktop.
- **Extensible**: Designed to be easily extended with more time-related tools.

## Prerequisites

- Python 3.10 or higher
- `pip` or `uv` for package management

## Usage with docker

```
{
  "mcpServers": {
    "time_server": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "harshpreet931/time_server"
      ]
    }
  }
}
```

## Setup and Installation

1.  **Clone the repository (or download the files):**
    ```bash
    # If this were a git repo already:
    # git clone <repository-url>
    # cd time-aware-mcp-server
    ```

2.  **Create a virtual environment (recommended):**
    Using `venv`:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
    ```
    Or using `uv`:
    ```bash
    uv venv
    source .venv/bin/activate # On Windows: .\.venv\Scripts\activate
    ```

3.  **Install dependencies:**
    Using `pip`:
    ```bash
    pip install "mcp[cli]"
    ```
    Or using `uv`:
    ```bash
    uv add "mcp[cli]"
    ```
    (You can also create a `requirements.txt` file with `mcp[cli]` and run `pip install -r requirements.txt` or `uv pip install -r requirements.txt`)

4.  **Run the server:**
    ```bash
    python time_server.py
    ```
    Or using `uv`:
    ```bash
    uv run time_server.py
    ```

## Configure MCP Client (Example: Claude for Desktop)

To use this server with an MCP client like Claude for Desktop, you need to add its configuration to the client's settings file.

1.  Locate your Claude for Desktop configuration file:
    *   **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
    *   **Windows**: `%APPDATA%\Claude\claude_desktop_config.json` (e.g., `C:\Users\<YourUser>\AppData\Roaming\Claude\claude_desktop_config.json`)
    *   **Linux**: `~/.config/Claude/claude_desktop_config.json`

2.  Add the server configuration to the `mcpServers` object. Replace `/absolute/path/to/` with the actual absolute path to your `time_server.py` file.

    ```json
    {
      "mcpServers": {
        "time_server": {
          "command": "python",
          "args": [
            "/absolute/path/to/time_server.py"
          ]
        }
        // Add other servers here if you have them
      }
    }
    ```
    **Important**: Ensure the path to `time_server.py` is correct. If you are running the server from within a virtual environment, the `python` command should ideally point to the Python interpreter in that virtual environment, or you should ensure the `mcp` library is globally accessible if not using a venv path in the command. For simplicity, the example uses `python`, assuming it's in your PATH and can find the `mcp` library.

## Usage

Once the server is running and the MCP client is configured, you can ask the AI agent to use the tool.

**Example Query:**

"What is the time part of 2025-06-09T16:30:00Z?"

**Expected Response from the tool (via the agent):**

"16:30:00"

**Error Handling:**

If an invalid date-time format is provided, the tool will return:
"Invalid date-time format. Please use ISO 8601 format."

## Contributing

Contributions are welcome! If you'd like to add more time-related tools or improve existing functionality, please feel free to fork the repository, make your changes, and submit a pull request.

When contributing, please ensure:
- Code is well-documented.
- New tools are tested.
- You follow the existing coding style.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
