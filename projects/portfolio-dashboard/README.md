# Project Blueprint: Portfolio Monitoring Dashboard

## Project goal
Build a decision-focused portfolio dashboard for exposure, delinquency, and concentration risk.

## Who it is for
Portfolio managers, risk leads, and executive stakeholders.

## Problem statement
Portfolio risk can accumulate silently without timely and clear monitoring signals.

## Suggested data schema
- reporting_date, product, region
- active_accounts, exposure_usd
- par30_pct, par90_pct, chargeoff_pct
- vintage_bucket

## Example features
- Trend features for PAR and charge-off
- Concentration by product/region
- Vintage roll-rate summaries

## Model / rules ideas
- Threshold-based traffic light statuses
- Early-warning risk scoring overlays

## Dashboard or UI ideas
- KPI summary cards
- Drill-down by segment/vintage
- Trend and variance views
- AI narrative summary panel

## Explainability considerations
- Include metric definitions in UI
- Attach data timestamp and source notes
- Separate narrative from observed facts

## Evaluation metrics
- Dashboard load and usability
- Decision usefulness from stakeholder feedback
- Alert precision for threshold flags

## Future enhancements
- Scenario analysis and stress tests
- Email/slack risk digests
- Portfolio comparison views

## Why this project is portfolio-worthy
It demonstrates business communication, data storytelling, and risk analytics engineering.
