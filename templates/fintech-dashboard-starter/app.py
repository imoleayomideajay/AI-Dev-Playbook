import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Fintech Dashboard Starter", layout="wide")

st.title("Fintech Portfolio Dashboard Starter")
st.caption("Beginner-friendly foundation for risk and monitoring dashboards")

df = pd.read_csv("sample_data.csv")

with st.sidebar:
    st.header("Filters")
    product = st.selectbox("Product", ["All"] + sorted(df["product"].unique().tolist()))

filtered = df if product == "All" else df[df["product"] == product]

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Active Loans", int(filtered["active_loans"].iloc[-1]))
kpi2.metric("Exposure (USD)", f"${int(filtered['exposure_usd'].iloc[-1]):,}")
kpi3.metric("PAR30", f"{filtered['par30_pct'].iloc[-1]:.1f}%")

fig = px.line(filtered, x="month", y="par30_pct", color="product", markers=True, title="PAR30 Trend")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Data preview")
st.dataframe(filtered, use_container_width=True)

st.subheader("AI Insight (Placeholder)")
st.info("AI insight example: PAR30 has trended upward. Review segment-level drivers and threshold alerts.")
