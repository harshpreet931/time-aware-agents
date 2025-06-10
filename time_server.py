from mcp.server.fastmcp import FastMCP
from datetime import datetime
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP("time_server")

@mcp.tool()
def time_now() -> str:
    """
    Get the current time in ISO 8601 format.

    Args:
        None

    Returns:
        str: The time component in ISO 8601 format (e.g., "16:30:00").
    """
    return datetime.now().time().isoformat()

if __name__ == "__main__":
    logger.info("Starting the time server...")
    mcp.run(transport='stdio')