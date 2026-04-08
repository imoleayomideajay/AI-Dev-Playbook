# Data Governance Checklist

## Data provenance
- [ ] Data sources are identified and documented
- [ ] Data extraction date/time is recorded

## Privacy
- [ ] Sensitive fields are minimized or masked
- [ ] Public/demo repositories avoid production PII

## Labeling assumptions
- [ ] Label definitions are explicit
- [ ] Label delay and noise risks are documented

## Feature documentation
- [ ] Feature definitions and transformations are recorded
- [ ] Known leakage risks are reviewed

## Validation
- [ ] Input validation checks are implemented
- [ ] Reconciliation to source totals is performed

## Monitoring
- [ ] Data freshness checks exist
- [ ] Drift indicators are defined

## Access control
- [ ] Access roles are defined for sensitive data
- [ ] Secrets are managed outside repository files

## Retention thinking
- [ ] Retention period assumptions are documented
- [ ] Data deletion/archive approach is considered
