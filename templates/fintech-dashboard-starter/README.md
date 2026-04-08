# Fintech Dashboard Starter

Starter template for portfolio and risk monitoring dashboards.

## What this template does
- Loads `sample_data.csv`
- Displays KPI cards
- Adds sidebar filtering by product
- Shows a simple trend chart
- Includes placeholder AI insight panel

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Suggested improvements
- Connect warehouse data
- Add delinquency cohort views
- Add alerts and threshold status logic
