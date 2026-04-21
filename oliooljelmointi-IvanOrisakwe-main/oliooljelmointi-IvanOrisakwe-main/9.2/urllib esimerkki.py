# urllib example: fetch and print Google's homepage
from urllib.request import urlopen, Request
import sys

response = None

try:
    # Google may block default urllib requests, so we set a User-Agent
    req = Request(
        "https://www.google.com",
        headers={"User-Agent": "Mozilla/5.0 (compatible; urllib-example/1.0)"}
    )
    response = urlopen(req, timeout=10)

except Exception as ex:
    # Print the error to stderr if fetching fails
    print(ex, file=sys.stderr)

else:
    # Read the raw HTML data
    data = response.read()

    # Try to detect charset from headers, default to utf-8
    charset = response.headers.get_content_charset() or "utf-8"

    # Decode bytes to string and print
    html = data.decode(charset, errors="replace")
    print(html)

finally:
    if response is not None:
        response.close()
