from mcp.server.fastmcp import FastMCP
from datetime import datetime
import logging
import sys
import pytz

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

@mcp.tool()
def time_now_with_timezone(timezone: str = "UTC") -> str:
    """
    Get the current time in the specified timezone in ISO 8601 format.

    Args:
        timezone: The timezone name (e.g., "America/New_York", "Europe/London", "Asia/Tokyo").
                 Defaults to "UTC" if not specified.

    Returns:
        str: The time in ISO 8601 format with timezone information.
    """
    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz)
        return current_time.isoformat()
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Error: Unknown timezone '{timezone}'. Please use a valid timezone name (e.g., 'America/New_York')."

if __name__ == "__main__":
    logger.info("Starting the time server...")
    mcp.run(transport='stdio')