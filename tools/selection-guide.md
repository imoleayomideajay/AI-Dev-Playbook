# Tool Selection Guide

Use this guide to choose a practical AI-building stack based on what you are trying to ship.

## 1) Clarify your build profile

Pick one primary profile:

- **Fast MVP**: You need a working prototype in days.
- **Data Product**: You need analytics, dashboards, and model explainability.
- **Engineering Control**: You need maintainable architecture and deeper customization.

## 2) Recommended starting stacks

### Fast MVP
- Build: Lovable or Bolt
- Code assist: Codex or Cursor
- Dashboard layer: Streamlit (if data-heavy)

### Data Product
- App layer: Streamlit
- Coding support: Copilot/Codex/Cursor
- Versioning + collaboration: GitHub

### Engineering Control
- Primary environment: Cursor or Windsurf
- Agentic execution: Codex
- Deployment: your preferred cloud CI/CD path

## 3) Evaluate before committing

Run a short benchmark sprint using:
- Time to first usable demo
- Ease of debugging
- Deployment readiness
- Reproducibility for teammates

Template: [`../benchmarks/benchmark-framework.md`](../benchmarks/benchmark-framework.md)

## 4) Common anti-patterns

- Picking tools by hype instead of constraints
- Ignoring onboarding needs for less-experienced teammates
- Optimizing for demo speed while neglecting maintainability
- Shipping without reproducible setup documentation
