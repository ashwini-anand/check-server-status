import asyncio
from server import check_server_status

async def run_tests():
    print("--- Running Server Status Checker Tests (FastMCP) ---")
    
    # Test 1: Active site (HTTPS)
    print("\nTest 1: Active site (google.com)")
    print(await check_server_status("google.com"))
    
    # Test 2: Active site (with HTTP protocol prefix)
    print("\nTest 2: Active site (http://example.com)")
    print(await check_server_status("http://example.com"))

    # Test 3: Invalid Domain / Hostname
    print("\nTest 3: Invalid domain name")
    print(await check_server_status("this-domain-surely-does-not-exist-12345.com"))

    # Test 4: Broken URL input
    print("\nTest 4: Invalid URL format")
    print(await check_server_status("http://"))

if __name__ == "__main__":
    asyncio.run(run_tests())
