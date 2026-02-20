import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000/wiki-search"

st.set_page_config(page_title="Knowledgebase Search", layout="centered")

st.title("Knowledgebase & Summarization Demo")

query = st.text_input("Enter your query:")
summary_length = st.selectbox(
    "Summary length",
    ["short", "medium", "long"],
    index=1
)

if st.button("Search"):
    if not query.strip():
        st.warning("Please enter a query")
    else:
        with st.spinner("Generating summary..."):
            try:
                response = requests.post(
                    FASTAPI_URL,
                    json={
                        "query": query,
                        "summary_length": summary_length
                    },
                    timeout=60
                )

                if response.status_code == 200:
                    data = response.json()
                    st.subheader("Summary")
                    st.write(data["summary"])
                else:
                    st.error(response.text)

            except Exception as e:
                st.error(f"Connection error: {e}")