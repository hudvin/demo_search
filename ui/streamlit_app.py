import os

import streamlit as st
import requests

FLASK_ENDPOINT_HOST = os.getenv("FLASK_ENDPOINT", "http://127.0.0.1:5000")
FLASK_ENDPOINT = f"{FLASK_ENDPOINT_HOST}/search"


def search(query:str):
    params = {"query": query}
    response = requests.get(FLASK_ENDPOINT, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return [{"error": f"Error {response.status_code}"}]


st.title("Search Engine Web App")

query = st.text_input("Enter your query:")

if st.button("Search"):
    if query:
        st.write(f"Searching for: {query}")
        results = search(query)

        for result in results:
            if "error" in result:
                st.error(result["error"])
            else:
                st.write(f"Similarity: {result['similarity']:.4f}")
                original_doc = result.get("original_document", {})
                st.write(f"Article Name: {original_doc.get('article_name', 'N/A')}")
                st.write(f"Article URL: {original_doc.get('link', 'N/A')}")
                st.write(
                    f"Text Content: {original_doc.get('text_content', 'N/A')[:150]}")  # show first 150 symbols
                st.write("\n---\n")
    else:
        st.warning("Please enter a query.")
