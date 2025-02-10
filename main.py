import streamlit as st
from scrape import (scrape_website, split_dom_content, clean_body_content, extract_body_content, )
from parse import parse_with_ollama

st.title("Business Web Scraper")
urls = st.text_area("Enter Website URLs (comma-separated):")

if st.button("Scrape Sites"):
    st.write("Scraping the websites")
    
    all_cleaned_content = []
    for url in urls.split(','):
        url = url.strip()
        if url:
            result = scrape_website(url)
            body_content = extract_body_content(result)
            cleaned_content = clean_body_content(body_content)
            all_cleaned_content.append(cleaned_content)
    
    st.session_state.dom_content = "\n".join(all_cleaned_content)

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", st.session_state.dom_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what kinds of businesses you are looking for")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")



            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
# .\ai\scripts\activate.ps1