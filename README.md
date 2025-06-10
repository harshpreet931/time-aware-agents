# Time-Aware MCP Server 🕒

Make your AI agents time-aware with this simple and efficient Model Context Protocol (MCP) server! This server provides a fundamental building block for time-sensitive AI applications by offering a tool to get the **current time**.

Built with Python and FastMCP, it's lightweight, easy to integrate, and ready to be extended with more sophisticated time-related functionalities.

## ✨ Key Features

-   **`time_now` Tool**: Instantly retrieve the current time in ISO 8601 format (e.g., "16:30:00").
-   **MCP Native**: Seamlessly integrates with MCP clients like Claude for Desktop, enabling AI agents to access real-time information.
-   **Lightweight & Fast**: Minimal overhead, ensuring quick responses.
-   **Easily Extensible**: A clean foundation to add more time-related tools (e.g., time zone conversions, date calculations, countdowns).
-   **Docker Ready**: Includes a Dockerfile for easy containerization and deployment (see Docker usage section below).
-   **Python Powered**: Leverages the robustness and flexibility of Python using FastMCP.

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

Once the server is running and the MCP client is configured, you can ask the AI agent to use the `time_now` tool.

**Example Interaction:**

*User to AI Agent:*
"What time is it now?" or "Can you get the current time using the time_now tool?"

*AI Agent (after using the `time_now` tool):*
The tool will return the current time, for example: "16:30:00" (depending on the actual current time).

**Error Handling:**

The `time_now` tool does not take any input parameters, so specific input validation errors are not applicable to the tool itself. General server or MCP communication errors would be handled by the MCP framework or the client.

## Contributing

Contributions are welcome! If you'd like to add more time-related tools or improve existing functionality, please feel free to fork the repository, make your changes, and submit a pull request.

When contributing, please ensure:
- Code is well-documented.
- New tools are tested.
- You follow the existing coding style.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
