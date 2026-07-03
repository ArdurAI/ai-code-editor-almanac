# OpenHands


[![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

| Attribute | Value |
|-----------|-------|
| Tier | A |
| Type | Autonomous agent |
| License | MIT |
| Region | Global |
| URL | https://github.com/All-Hands-AI/OpenHands |

## One-line summary

79K+ GitHub stars (formerly OpenDevin); the leading open-source autonomous AI software engineering agent with Docker-sandboxed execution, multi-model support, and SWE-bench leading performance.

## Architecture

OpenHands (formerly OpenDevin) is an open-source autonomous AI software engineering platform. Key architectural elements:

- **Docker-sandboxed execution**: Each agent runs in an isolated Docker container with shell, browser, and code editing capabilities
- **Agent loop**: Plans, acts (shell/file/browser), and observes results in an iterative loop
- **Multi-model**: Supports Claude, GPT, Gemini, local models — BYOK
- **Evaluation harness**: Built-in SWE-bench evaluation and custom benchmark support
- **Web UI**: Browser-based interface for monitoring and interacting with agents
- **Headless mode**: API/programmatic access for CI/CD integration
- **Runtime**: Configurable compute environments per task

## Key features

- 79K+ stars — most popular open-source autonomous coding agent
- Docker-sandboxed execution (shell, browser, file system)
- BYOK with Claude, GPT, Gemini, and local model support
- Built-in SWE-bench evaluation harness
- Web UI for monitoring agent work
- Headless/API mode for CI/CD integration
- MIT licensed — fully open source
- Custom agent support (code your own agent loop)
- Multi-agent orchestration

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Strong | SWE-bench Verified: 53%+ (with Claude Sonnet) |
| Latency | Variable | Autonomous tasks take minutes; depends on complexity |
| Token economics | Moderate | BYOK; autonomous loops consume significant tokens |
| Scale behavior | Strong | Docker isolation enables parallel task execution |
| Ops burden | Moderate | Docker setup required; more complex than CLI tools |
| Developer experience | Moderate | Web UI + CLI; Docker adds setup complexity |
| Data sovereignty | Strong | Self-hosted; BYOK; local model support |

## Ops reality

**Setup burden:** Moderate — requires Docker; clone repo, configure environment, start services.

**Sharp edges:**
- Docker setup adds complexity compared to CLI-only tools
- Autonomous tasks consume significant tokens
- Web UI is functional but less polished than commercial alternatives
- Configuration flexibility means more tuning required

## Cost model

- **Software**: Free (MIT open source)
- **Infrastructure**: Docker host (local or cloud)
- **API costs**: BYOK — depends on model chosen
- **Cloud deployment**: Optional cloud hosting costs if running on AWS/GCP/Azure

## When to use / when to avoid

**Use when:**
- You want the most capable open-source autonomous agent
- Self-hosting and data control are requirements
- You need SWE-bench evaluation and benchmarking
- Docker sandboxing fits your security model

**Avoid when:**
- You want minimal setup (use Claude Code or Aider)
- You need polished commercial UX
- Docker is not available in your environment

## Roster entry

- **Name:** OpenHands
- **Type:** Autonomous agent
- **License:** MIT
- **Region:** Global
- **Tier:** A
- **Notes:** 79K+ stars; formerly OpenDevin; Docker sandboxed

---

## Deep Analysis

### 1. How Is This Tool Useful?

OpenHands is the open-source alternative to Devin — a fully autonomous AI software engineering agent that runs in Docker-sandboxed environments. Its 79K+ GitHub stars (under the All-Hands-AI organization, formerly OpenDevin) make it the most popular open-source autonomous coding agent by a wide margin. For teams that want Devin-like autonomous capabilities without vendor lock-in or proprietary pricing, OpenHands is the natural choice.

The Docker-sandboxed execution model is both a security feature and a capability enabler. Each agent task runs in an isolated container with controlled access to shell, file system, and browser — preventing unintended damage to the host system while giving the agent the tools it needs for complex tasks. This makes OpenHands suitable for running untrusted or experimental code, and for CI/CD integration where agents handle automated tasks like bug fixing or test generation.

The built-in SWE-bench evaluation harness is a unique feature that makes OpenHands valuable beyond direct use. Teams and researchers use OpenHands to benchmark different models, agent configurations, and prompting strategies on standardized software engineering tasks. This has made OpenHands a reference platform for the open-source AI coding research community, contributing to rapid improvement in agent capabilities.

### 2. Gotchas of Using This Tool

Docker setup complexity is the primary barrier. Unlike CLI tools (Claude Code, Aider) that install with a single command, OpenHands requires Docker, Docker Compose, environment configuration, and container management. For developers unfamiliar with Docker, the initial setup can be daunting. The documentation is comprehensive but the complexity is inherent to the sandboxed architecture.

Token consumption on autonomous tasks is high. Because OpenHands agents run full autonomous loops (plan, act, observe, repeat), they consume significantly more tokens than interactive tools. A single SWE-bench task can consume 50K–200K+ tokens. Teams must budget for API costs carefully, especially when using expensive models like Claude Opus. Local models (via Ollama) reduce costs but may sacrifice quality.

The Web UI, while functional, is less polished than commercial alternatives like Devin's dashboard or Cursor's IDE. The interface works for monitoring agent progress and reviewing results, but it's clearly built by engineers for engineers. Organizations expecting a consumer-grade experience will need to adjust expectations.

### 3. Limitations

- **Docker requirement**: Adds setup complexity; not available in all environments
- **Token consumption**: Autonomous loops are expensive
- **UI polish**: Functional but less polished than commercial alternatives
- **Agent reliability**: While strong, complex tasks still fail and require human intervention
- **Speed**: Autonomous tasks take minutes; not real-time
- **Resource usage**: Docker containers consume CPU/RAM; running multiple agents requires substantial hardware
- **Configuration complexity**: Flexible configuration means more tuning required

### 4. How Secure Is This Tool?

- **License**: MIT (fully open source; auditable)
- **Docker sandboxing**: Strong isolation — agents cannot access host system beyond configured mounts
- **BYOK**: Code goes to your chosen model provider; OpenHands doesn't intermediate
- **Local model support**: Ollama integration for fully local operation
- **Self-hosted**: Full data control; nothing leaves your infrastructure with local models
- **Telemetry**: Optional; can be disabled
- **Known CVEs**: No major security advisories as of mid-2026
- **Code exfiltration risk**: Low with local models; moderate with cloud providers (you control)
- **Docker security**: Benefits from Docker's security model; can run rootless

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 1/10**

OpenHands is a developer/researcher tool requiring Docker knowledge, API key configuration, and understanding of autonomous agent concepts. Non-technical users cannot use it. The Web UI provides some accessibility but the underlying concepts require technical expertise.

### 6. What Does This Tool Solve That Others Don't?

OpenHands's unique advantages:

- **Open-source autonomous agent**: The most capable fully open-source alternative to Devin
- **Docker sandboxing**: Strong isolation for safe autonomous execution — rare among coding tools
- **SWE-bench evaluation harness**: Built-in benchmarking — invaluable for research and model comparison
- **Custom agent support**: Code your own agent loops — maximum flexibility for research
- **Self-hosted**: Full data sovereignty — no vendor lock-in
- **MIT license**: Most permissive license — maximum commercial and research freedom

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Key Advantage | Key Disadvantage |
|------|------|--------------|-----------------|
| 1 | Devin | Commercial polish; Slack integration | Proprietary; expensive; ACU costs |
| 2 | **OpenHands** | Open source; Docker sandbox; eval harness | Docker complexity; token costs |
| 3 | Claude Code | Best interactive agentic coding | Not autonomous; interactive only |
| 4 | Replit Agent | Cloud app building + deploy | Less flexible; app-focused |

### 8. How Can This Tool Be Improved? How Active Is Development?

**Development activity**: Extremely active. [OpenHands/OpenHands](https://github.com/All-Hands-AI/OpenHands) (redirected from All-Hands-AI/OpenHands) has **79,171 stars**, 10,076 forks, 341 open issues. Last pushed: July 2, 2026. Created March 2024 (as OpenDevin) — explosive growth.

**Areas for improvement:**
- Simplified setup (one-click Docker or cloud deployment)
- Reduced token consumption through better context management
- UI polish to match commercial alternatives
- Better agent reliability on complex, multi-step tasks
- More pre-built agent templates for common workflows
- Improved documentation for custom agent development
- Better integration with CI/CD pipelines (GitHub Actions, GitLab CI)

### 9. Official Maintainer Contacts

- **GitHub**: [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) (redirects to OpenHands/OpenHands)
- **Organization**: All-Hands-AI — https://www.all-hands.dev
- **Discord**: OpenHands Discord (link in GitHub README)
- **Twitter/X**: [@AllHandsAI](https://twitter.com/AllHandsAI)
- **Docs**: https://docs.all-hands.dev
- **Email**: contact@all-hands.dev

### 10. General Usage Guidance

**Getting started:**
1. Ensure Docker is installed and running
2. Clone: `git clone https://github.com/All-Hands-AI/OpenHands && cd OpenHands`
3. Configure: Set up environment variables (LLM API keys, etc.)
4. Run: `make build && make run` (or use Docker Compose)
5. Open the Web UI (typically http://localhost:3000)
6. Create a task and monitor the agent

**Best practices:**
- Start with simple tasks to calibrate model costs
- Use Docker resource limits to prevent runaway resource consumption
- Connect your GitHub/GitLab for code access
- Use the evaluation harness to benchmark different models
- Monitor token consumption per task
- Use local models for cost-sensitive or privacy-sensitive tasks
- Contribute custom agents back to the community

**When NOT to use:**
- If Docker is not available or you want minimal setup (use Claude Code)
- If you need real-time interactive coding (use Claude Code or Cursor)
- If token costs for autonomous tasks are prohibitive
- If you need commercial support and SLAs

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*
