# streamlit_app.py
import streamlit as st
from scraper_utils import get_html_playwright, extract_info

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
