# Playbook: Build a Data Dashboard with AI

## Who this is for
Data analysts and dashboard developers modernizing KPI dashboards with AI-assisted commentary.

## What you will build
A dashboard with filters, KPIs, trend views, and generated insights tied to visible source metrics.

## Why it matters
Decision-makers need interpretation plus transparent evidence, not disconnected AI text.

## Recommended stack
- Streamlit
- Pandas
- Plotly
- LLM API for narrative summaries

## Suggested folder structure
```text
dashboard/
├── app.py
├── charts/
├── transforms/
├── prompts/
└── data/
```

## Step-by-step workflow
1. Select 3-6 key business metrics.
2. Build baseline dashboard layout.
3. Add filtering and date controls.
4. Add AI summary blocks tied to visible numbers.
5. Add fallback behavior when AI is unavailable.
6. Validate summaries against historical known events.

## Data requirements
- Timestamped metric data
- Clean dimensions for filtering
- Data freshness indicator

## Core metrics or outputs
- KPI trends
- Variance vs prior period
- AI-generated summary with evidence references

## Common mistakes
- Hiding raw numbers behind narrative text
- Overloading with too many visuals
- No timestamp/data freshness cues

## Governance / responsible use considerations
- Separate factual metrics from generated commentary
- Keep summary prompts versioned
- Review AI narratives for misleading causal language

## Upgrade ideas
- Add anomaly alerts
- Add scheduled executive summary digest
- Add threshold-based traffic-light status cards

## Final takeaway
Useful AI dashboards combine interpretability, source visibility, and decision-focused design.
