from bs4 import BeautifulSoup


def extract_info(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string if soup.title else ""
    all_links = [a.get("href") for a in soup.find_all("a", href=True)]
    meta = {meta['name']: meta.get('content', '') for meta in soup.find_all('meta', attrs={'name': True})}
    text = soup.get_text(separator=' ', strip=True)
    return {
        "title": title,
        "links": all_links,
        "meta": meta,
        "main_text": text[:500] # Show only first 500 chars
    }
