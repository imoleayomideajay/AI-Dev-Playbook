# Tool Matrix

Qualitative comparison of common AI-assisted development tools and platforms.

> Ratings use **Low / Medium / High** and are intentionally qualitative to stay practical and transparent.

| Tool | Category | Best for | Skill level | Speed to MVP | Flexibility | Key advantage | Key limitation |
|---|---|---|---|---|---|---|---|
| Codex | Agentic coding assistant | Repo-level implementation and refactoring workflows | Intermediate | High | High | Strong for end-to-end code changes with context | Needs good prompting and review discipline |
| Cursor | AI-native IDE | Developers who want in-editor AI pair programming | Beginner–Intermediate | High | High | Tight IDE workflow and fast iteration | Can encourage over-reliance without architecture planning |
| Replit | Cloud dev platform | Rapid prototyping and quick sharing | Beginner | High | Medium | Zero-setup environment and easy collaboration | Less control for advanced production architecture |
| Lovable | AI app builder | Non-experts shipping UI-first products quickly | Beginner | High | Medium | Fastest path from idea to visible app | Limited depth for complex backend logic |
| Streamlit | Python app framework | Data apps and analytics dashboards | Beginner–Intermediate | High | Medium | Excellent for data workflows and demo-to-MVP path | UI customization ceiling vs full frontend stacks |
| GitHub Copilot | Code completion assistant | General coding productivity in existing IDEs | Beginner–Advanced | Medium | High | Broad language support with low friction adoption | Not a full workflow orchestrator by itself |
| Windsurf | AI development environment | AI-assisted coding with integrated agent workflows | Intermediate | High | High | Strong autonomous coding flows in one workspace | Team standards required to keep output consistent |
| Bolt | Prompt-to-app builder | Fast web app scaffolding from ideas | Beginner | High | Medium | Rapid generation of working app skeletons | Generated output often needs structural hardening |
| v0 | UI generation tool | Fast component and interface prototyping | Beginner–Intermediate | High | Medium | Excellent speed for modern UI mockups/components | Primarily frontend-focused; backend still required |

## How to use this matrix

1. Start with your delivery constraint (speed, control, or team maintainability).
2. Pick one primary build tool and one supporting tool.
3. Validate your choice with the benchmark framework in [`../benchmarks/benchmark-framework.md`](../benchmarks/benchmark-framework.md).
