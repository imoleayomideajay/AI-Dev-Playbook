# Playbook: Build a Fraud Detection System

## Who this is for
Fintech risk analysts and engineers building practical fraud alerting workflows.

## What you will build
A fraud detection pipeline with rule-based screening, model risk scoring, and analyst review support.

## Why it matters
Fraud systems fail when they optimize only model metrics and ignore operational review burden.

## Recommended stack
- Python + Pandas
- scikit-learn or XGBoost
- Streamlit for analyst case views
- SQL store for events and decisions

## Suggested folder structure
```text
fraud-system/
├── data/
├── features/
├── rules/
├── models/
├── dashboard/
└── monitoring/
```

## Step-by-step workflow
1. Define fraud objective and alert SLAs.
2. Build baseline rules (velocity, location mismatch, device anomalies).
3. Prepare labeled data and handle class imbalance.
4. Train model and compare against rule-only baseline.
5. Design decision thresholds for false-positive tolerance.
6. Build review queue UI and analyst feedback capture.
7. Track drift and recalibration cadence.

## Data requirements
- Transaction events with timestamps
- Outcome labels (chargeback/fraud confirmed)
- Device, identity, merchant context

## Core metrics or outputs
- Precision, recall, PR-AUC
- False-positive rate
- Analyst workload per day
- Time-to-investigation

## Common mistakes
- Ignoring class imbalance handling
- No threshold governance process
- No feedback loop from analysts

## Governance / responsible use considerations
- Document label quality and delays
- Log rule/model versions per decision
- Add human review for high-impact blocks

## Upgrade ideas
- Graph/entity-link fraud detection
- Segment-specific thresholds
- Champion-challenger model testing

## Final takeaway
Fraud detection is a socio-technical system: model quality, thresholds, and review operations must work together.
