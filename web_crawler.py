import streamlit as st
from get_html_playwright import get_html_playwright # Make sure this path is correct
from beautiful_soup import extract_info # Make sure this path is correct
import traceback

st.title("Web Crawler Agent")

url = st.text_input("Enter a webpage URL:")

if st.button("Crawl"):
    with st.spinner("Crawling..."):
        try:
            st.write(f"Fetching URL: {url}")
            html = get_html_playwright(url)
            result = extract_info(html)
            st.write("## Page Title:", result["title"])
            st.write("## Meta Data:", result["meta"])
            st.write("## Links:", result["links"])
            st.write("## Main Text:", result["main_text"])
        except Exception as e:
            print(traceback.format_exc()) # Full stack trace to terminal
            st.error(f"Error: {e}") # Error details to Streamlit UI