# Playbook: Build a Loan Portfolio Dashboard

## Who this is for
Risk teams and analytics engineers creating executive-level portfolio monitoring tools.

## What you will build
A dashboard for delinquency, exposure, vintage performance, and concentration risk monitoring.

## Why it matters
Portfolio visibility supports proactive risk decisions before losses compound.

## Recommended stack
- Streamlit
- Pandas + Plotly
- SQL warehouse extracts
- Optional AI summary panel

## Suggested folder structure
```text
loan-portfolio-dashboard/
├── app.py
├── kpis/
├── charts/
├── data/
└── insights/
```

## Step-by-step workflow
1. Define executive KPI pack.
2. Build ingestion and validation for periodic snapshots.
3. Create KPI cards and trend charts.
4. Add segmentation filters (product, region, vintage).
5. Add placeholder AI insights tied to visible metrics.
6. Add alert thresholds and status indicators.

## Data requirements
- Loan-level balances and status
- Payment history and delinquency buckets
- Product and geography attributes

## Core metrics or outputs
- PAR30/PAR90
- Roll rates
- Charge-off rate
- Exposure concentration

## Common mistakes
- No consistent reporting cut date
- Confusing definitions across metrics
- No reconciliation to source totals

## Governance / responsible use considerations
- Standardize metric definitions
- Track refresh lineage and timestamps
- Separate generated commentary from factual KPIs

## Upgrade ideas
- Early warning score overlays
- Cohort drill-down views
- Portfolio stress scenario panels

## Final takeaway
Portfolio dashboards are decision tools: clarity, consistency, and trust matter more than visual complexity.
