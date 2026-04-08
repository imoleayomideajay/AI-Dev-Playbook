import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Dev Playbook Starter", layout="wide")

st.title("AI Dev Playbook · Streamlit Starter")
st.caption("Minimal, portfolio-ready starter for AI-assisted analytics apps")

with st.sidebar:
    st.header("Settings")
    tone = st.selectbox("Response style", ["Concise", "Analyst", "Executive"])
    st.markdown("Use synthetic data for public demos.")

left, right = st.columns([2, 1])

with left:
    prompt = st.text_area("Ask a question", placeholder="Summarize portfolio risk changes this week")
    if st.button("Generate AI response"):
        if prompt.strip():
            st.success("Placeholder AI response")
            st.write(f"Style: **{tone}**")
            st.write("This section will show model output with references to visible metrics.")
        else:
            st.warning("Please enter a prompt first.")

with right:
    st.subheader("Quick KPIs")
    st.metric("Active Loans", "4,820")
    st.metric("PAR30", "3.9%")
    st.metric("Charge-off Rate", "1.2%")

st.subheader("Sample dataframe")

df = pd.DataFrame(
    {
        "segment": ["Prime", "Near Prime", "Subprime", "SME"],
        "exposure_usd": [2_400_000, 1_650_000, 980_000, 720_000],
        "par30_pct": [1.8, 3.2, 7.1, 4.6],
    }
)

st.dataframe(df, use_container_width=True)
