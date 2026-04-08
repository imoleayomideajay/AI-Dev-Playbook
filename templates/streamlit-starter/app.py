import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Dev Playbook Starter", layout="wide")

st.title("AI Dev Playbook · Streamlit Starter")
st.caption("Minimal starter for AI-assisted dashboard apps")

user_input = st.text_area("Enter your prompt", placeholder="Summarize last week performance trends")

if st.button("Generate response"):
    if user_input.strip():
        st.success("Placeholder AI response")
        st.write(
            "This is where your model output will appear. "
            "Connect your preferred AI provider and add structured prompt handling."
        )
    else:
        st.warning("Please enter a prompt first.")

st.subheader("Sample data preview")

sample_df = pd.DataFrame(
    {
        "metric": ["Revenue", "Transactions", "Conversion Rate", "Chargebacks"],
        "value": [125000, 4820, 0.042, 37],
        "period": ["Last 30 days"] * 4,
    }
)

st.dataframe(sample_df, use_container_width=True)
