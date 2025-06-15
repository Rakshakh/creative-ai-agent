import streamlit as st
import requests

st.set_page_config(page_title="Creative AI Agent", page_icon="🧠")
st.title("🤖 Creative AI Agent")

st.markdown("Your personal co-founder that helps you ideate, plan, and execute like Musk x Balaji x Da Vinci.")

# --- UI Components ---
option = st.selectbox("🔧 Choose a Command", ["/storm", "/map"])
input_text = st.text_area("📝 Input Theme or Idea")

# --- Backend Call ---
if st.button("🚀 Run Command"):
    if not input_text.strip():
        st.warning("Please enter a theme or idea first.")
    else:
        endpoint = "http://localhost:5000/storm" if option == "/storm" else "http://localhost:5000/map"
        payload = {"theme": input_text} if option == "/storm" else {"idea": input_text}

        try:
            res = requests.post(endpoint, json=payload)
            res.raise_for_status()  # Raise error for bad HTTP responses (4xx, 5xx)
            try:
                st.success("✅ Response received!")
                st.json(res.json())
            except Exception as json_err:
                st.error("❌ Failed to parse response as JSON.")
                st.text(res.text)
        except requests.exceptions.RequestException as req_err:
            st.error("❌ Request failed. Is your backend running?")
            st.text(str(req_err))
