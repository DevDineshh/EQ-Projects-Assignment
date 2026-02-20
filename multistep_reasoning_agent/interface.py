import streamlit as st
import requests  # new import

st.title("Multi-Step Reasoning Agent")

question = st.text_area("Enter your question:")

if st.button("Solve"):
    if question.strip():
        # Call FastAPI backend
        try:
            response = requests.post(
                "http://127.0.0.1:8000/solve",
                json={"question": question}
            )
            result = response.json()
            
            st.subheader("Answer")
            st.write(result.get("answer", "No answer"))

            st.subheader("Reasoning")
            st.write(result.get("reasoning_visible_to_user", ""))

            # # Optional: show metadata
            # st.subheader("Metadata")
            # st.json(result.get("metadata", {}))

        except Exception as e:
            st.error(f"Error calling backend: {e}")