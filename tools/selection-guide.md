# Tool Selection Guide

Use this guide to choose the right AI development stack for your project stage and team profile.

## Step 1: Identify your primary objective

- **Learn quickly:** prioritize beginner-friendly tools with fast feedback loops.
- **Ship MVP fast:** choose high speed-to-MVP tools and simple deployment paths.
- **Build scalable product:** prioritize flexibility, governance, and architecture control.

## Step 2: Match your builder profile

- **Data analyst / dashboard builder:** start with Streamlit + an AI coding assistant.
- **Solo app builder:** use a rapid builder (Replit, Lovable, Bolt, v0) and harden later.
- **Engineering team:** use IDE-centric workflows (Codex, Cursor, Copilot, Windsurf) with CI/CD.

## Step 3: Decide your workflow pattern

### Pattern A: Fast prototype
- Tools: Replit + Lovable/Bolt + Streamlit
- Best when: validating demand in days, not weeks

### Pattern B: Structured builder workflow
- Tools: Cursor or Windsurf + GitHub + Streamlit
- Best when: balancing speed and maintainability

### Pattern C: Engineering-grade foundation
- Tools: Codex/Cursor + Copilot + GitHub Actions
- Best when: you need stronger review, testing, and long-term extensibility

## Step 4: Validate with a benchmark sprint

Before standardizing:
- run a 1-week pilot
- measure time to MVP
- compare quality of output and debugging friction
- evaluate reproducibility for new contributors

Use: [Benchmark Framework](../benchmarks/benchmark-framework.md)

## Common selection mistakes

- Choosing tools based on trends instead of constraints
- Mixing too many tools without clear ownership
- Ignoring deployment and maintenance implications
- Skipping documented evaluation criteria

## Recommended default for most builders

For beginner-to-intermediate builders shipping practical apps:

- **Build layer:** Streamlit
- **Coding assist:** Cursor or Codex
- **Versioning:** GitHub
- **Evaluation:** this repo's benchmark framework

Then evolve only after real bottlenecks appear.
