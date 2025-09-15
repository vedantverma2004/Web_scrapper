def get_html_playwright(url):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        html = page.content()
        browser.close()
    return html

if __name__ == "__main__":
    url = "https://example.com"
    html = get_html_playwright(url)
    print(html[:1000]) # Print just the first 1000 characters for readability