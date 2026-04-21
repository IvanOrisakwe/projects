# app.py
# Use WebData to fetch Google and print the <head>...</head> section.

from oliot import WebData

def tulosta_googlen_head():
    url = "https://www.google.com"
    web = WebData(url)

    # Get raw HTML once via our API
    html = web.PalautaRaaka()

    # Find <head>...</head> (case-insensitive, robust to <head ...>)
    lower = html.lower()
    start = lower.find("<head")
    if start == -1:
        print("No <head> found.")
        return

    # End of opening <head ...> tag
    open_end = html.find('>', start)
    if open_end == -1:
        print("Malformed <head> tag.")
        return

    # Closing </head>
    close = lower.find("</head>", open_end)
    if close == -1:
        print("No </head> found.")
        return

    head_html = html[start: close + len("</head>")]
    print(head_html)

if __name__ == "__main__":
    tulosta_googlen_head()
