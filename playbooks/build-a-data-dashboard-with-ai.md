# Playbook: Build a Data Dashboard with AI

## Who this is for
- Data analysts building self-service analytics apps
- Dashboard developers adding natural-language interaction
- Teams that need faster insight exploration

## What you will build
A dashboard that combines:
- core KPI visualizations
- natural-language query support
- AI-assisted interpretation of trends and anomalies

## Recommended stack
- UI: Streamlit
- Data processing: Pandas + SQL
- Visualization: Plotly or Altair
- AI layer: LLM function for chart explanations and question answering
- Storage: CSV/Parquet initially, warehouse later

## Workflow
1. **Define the decision workflow**
   - What decisions should users make from this dashboard?
2. **Lock KPI definitions**
   - Ensure metrics are unambiguous before adding AI interpretation.
3. **Build deterministic charts first**
   - Time series, segment comparison, and variance views.
4. **Add guided AI prompts**
   - Example buttons: “What changed?”, “What should I investigate?”
5. **Constrain AI context**
   - Pass only relevant metrics and recent windows to avoid hallucinations.
6. **Add traceability**
   - Show which metrics/time range informed each AI response.
7. **Pilot with real users**
   - Capture misunderstood outputs and refine prompt structure.

## Common mistakes
- Letting AI generate metrics without source-of-truth definitions
- Passing raw, high-volume tables directly into prompts
- Hiding assumptions behind prose outputs
- Skipping user testing on explanation clarity

## Upgrade ideas
- Add anomaly detection module with threshold tuning
- Add role-based views for exec, ops, and analyst personas
- Add scheduled insight digests via email or Slack
- Add cache and query optimization for scale

## Final takeaway
Great AI dashboards pair trustworthy metrics with constrained AI interpretation. Deterministic analytics remains the backbone; AI accelerates insight communication.
