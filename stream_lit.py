# scraper_utils.py
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def get_html_playwright(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        html = page.content()
        browser.close()
    return html

def extract_info(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string if soup.title else ""
    all_links = [a.get("href") for a in soup.find_all("a", href=True)]
    
    # Safe extraction of meta tags
    meta = {}
    for meta_tag in soup.find_all("meta", attrs={"name": True}):
        name = meta_tag.get("name")
        content = meta_tag.get("content", "")
        if name:
            meta[name] = content

    text = soup.get_text(separator=' ', strip=True)
    return {
        "title": title,
        "links": all_links,
        "meta": meta,
        "main_text": text[:500]  # Show only first 500 chars
    }


# streamlit_app.py
import streamlit as st
# from scraper_utils import get_html_playwright, extract_info

st.set_page_config(page_title="Web Scraper", layout="wide")
st.title("🌐 Web Scraper using Playwright + BeautifulSoup")

url = st.text_input("Enter a URL to scrape", "https://example.com")

if st.button("Scrape"):
    with st.spinner("Fetching and parsing HTML..."):
        try:
            html = get_html_playwright(url)
            data = extract_info(html)

            st.subheader("Page Title")
            st.write(data["title"])

            st.subheader("Meta Tags")
            st.json(data["meta"])

            st.subheader("Links Found")
            st.write(data["links"])

            st.subheader("Main Text (First 500 chars)")
            st.write(data["main_text"])

        except Exception as e:
            st.error(f"Error occurred: {e}")
