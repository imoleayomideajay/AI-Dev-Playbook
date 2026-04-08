import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Dev Playbook Starter", page_icon="🤖", layout="centered")

st.title("🤖 AI Dev Playbook - Streamlit Starter")
st.caption("Minimal starter for AI-assisted apps and data dashboards")

user_prompt = st.text_input("Enter a prompt", placeholder="Explain this week's KPI movement in simple language")

if st.button("Generate response"):
    if user_prompt.strip():
        placeholder_response = (
            "This is a placeholder AI response. "
            "Replace this block with your model/API integration logic."
        )
        st.success("Response generated")
        st.write(placeholder_response)
    else:
        st.warning("Please enter a prompt before generating a response.")

st.subheader("Sample DataFrame")
example_df = pd.DataFrame(
    {
        "metric": ["Revenue", "Active Users", "Churn"],
        "value": [125000, 4210, 0.034],
        "period": ["2026-W14", "2026-W14", "2026-W14"],
    }
)
st.dataframe(example_df, use_container_width=True)
