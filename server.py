import time
from urllib.parse import urlparse
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("Server Status Checker")

@mcp.tool()
async def check_server_status(url: str, timeout: float = 10.0) -> str:
    """Check if a website or service is up or down by sending a GET request.

    Args:
        url: The URL to check (e.g., "https://github.com" or "google.com").
        timeout: Request timeout in seconds (default: 10.0).
    """
    # Normalize the URL if protocol is missing
    clean_url = url.strip()
    if not clean_url.startswith(("http://", "https://")):
        clean_url = "https://" + clean_url

    # Basic validation of URL structure
    try:
        parsed = urlparse(clean_url)
        if not parsed.netloc:
            return f"❌ Invalid URL: '{url}'. Please provide a valid hostname or web address."
    except Exception as e:
        return f"❌ Failed to parse URL '{url}': {str(e)}"

    start_time = time.perf_counter()
    try:
        # Use a modern user-agent to prevent getting blocked by basic anti-bot rules
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 (MCP-Server-Status-Checker)"
        }
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=True, headers=headers) as client:
            response = await client.get(clean_url)
            elapsed_time = (time.perf_counter() - start_time) * 1000
            
            # Status codes in the 2xx and 3xx ranges indicate success/redirection.
            is_up = response.status_code < 400
            status_indicator = "🟢 UP" if is_up else "🔴 DOWN (HTTP Error)"
            
            summary = [
                f"Status: {status_indicator}",
                f"Checked URL: {clean_url}",
                f"HTTP Code: {response.status_code} ({response.reason_phrase})",
                f"Response Time: {elapsed_time:.1f} ms"
            ]
            return "\n".join(summary)

    except httpx.HTTPStatusError as e:
        elapsed_time = (time.perf_counter() - start_time) * 1000
        return (
            f"🔴 DOWN (HTTP Status Error)\n"
            f"Checked URL: {clean_url}\n"
            f"HTTP Code: {e.response.status_code}\n"
            f"Response Time: {elapsed_time:.1f} ms\n"
            f"Error Details: {str(e)}"
        )
    except httpx.ConnectTimeout:
        return f"🔴 DOWN (Connection Timeout)\nChecked URL: {clean_url}\nError: Server took longer than {timeout}s to respond."
    except httpx.ConnectError:
        return f"🔴 DOWN (Connection Error)\nChecked URL: {clean_url}\nError: Could not resolve hostname or establish connection."
    except httpx.RequestError as e:
        return f"🔴 DOWN (Request Error)\nChecked URL: {clean_url}\nError: {str(e)}"

if __name__ == "__main__":
    # Run the server using stdio transport (standard for MCP clients)
    mcp.run(transport="stdio")
