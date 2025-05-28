import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="Sentiment Insight Tool", layout="centered")

st.title("🧠 Product Review Sentiment Analysis")

with st.expander("📊 Evaluate Dataset Metrics"):
    if st.button("Run Evaluation"):
        res = requests.get(f"{BASE_URL}/metrics").json()
        st.json(res)

st.subheader("💬 Analyze a New Review")

review_input = st.text_area("Enter customer review:")
if st.button("Analyze"):
    if review_input:
        response = requests.post(f"{BASE_URL}/analyze", json={"message": review_input}).json()
        st.write("### 🔍 Input Review")
        st.success(response["input"])
        st.write("### 📑 Similar Reviews & Predictions")
        for r in response["analysis"]:
            st.markdown(f"- **Predicted**: `{r['predicted']}` | **Actual**: `{r['actual']}`")
            st.code(r["example"])
    else:
        st.warning("Please enter some text to analyze.")
