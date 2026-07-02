# Cody

| Attribute | Value |
|-----------|-------|
| Tier | B |
| Type | Codebase assistant |
| License | Proprietary |
| Region | US |
| URL | https://cody.sourcegraph.com |

## One-line summary

Sourcegraph's AI coding assistant; specializes in large-codebase understanding with deep code search, multi-repo context, and enterprise code intelligence; $9–19/mo.

## Architecture

Cody is Sourcegraph's AI coding assistant, leveraging Sourcegraph's code intelligence infrastructure. Key architectural elements:

- **Code graph**: Uses Sourcegraph's code search and indexing infrastructure to understand relationships across large codebases
- **Multi-repo context**: Can search and reference code across multiple repositories
- **Multi-model**: Supports Claude, GPT, Gemini, and custom models
- **IDE integration**: VS Code and JetBrains extensions
- **Enterprise code intelligence**: Leverages Sourcegraph's enterprise code search platform
- **Context retrieval**: Advanced retrieval augmented generation (RAG) over code graphs
- **Codebase embeddings**: Creates embeddings of your entire codebase for semantic search

## Key features

- Deep codebase understanding via Sourcegraph's code intelligence
- Multi-repository search and context (unique capability)
- Multi-model support (Claude, GPT, Gemini)
- VS Code and JetBrains support
- Enterprise features: SSO, audit logs, on-prem option
- Code search and navigation (Sourcegraph heritage)
- Embeddings-based semantic code search
- Custom model support (enterprise)

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Not publicly available | Strength is codebase understanding, not raw coding |
| Latency | Not run | Code graph queries add latency |
| Token economics | Not run | Subscription-based |
| Scale behavior | Excellent | Best-in-class for very large codebases (Sourcegraph's strength) |
| Ops burden | Low (cloud) / Moderate (enterprise) | Enterprise requires Sourcegraph instance |
| Developer experience | Moderate | Good for search; less polished for coding assistance |
| Data sovereignty | Partial | Enterprise on-prem available |

## Ops reality

**Setup burden:** Low (cloud) — install extension, authenticate. Moderate (enterprise) — requires Sourcegraph instance.

**Sharp edges:**
- Less polished coding assistance than Cursor or Copilot
- Best value requires Sourcegraph enterprise infrastructure
- Multi-repo features need enterprise tier
- Smaller community than Copilot/Cursor

## Cost model

| Plan | Price | Key features |
|------|-------|-------------|
| Free | $0 | Limited usage; single repo |
| Pro | $9/mo | More usage; multi-model |
| Enterprise | $19/user/mo | Full code graph; multi-repo; on-prem |
| Enterprise+ | Custom | Custom models; dedicated support |

## When to use / when to avoid

**Use when:**
- You have a very large codebase (millions of LOC)
- Multi-repository code understanding is critical
- You already use Sourcegraph for code search
- Enterprise code intelligence is a requirement

**Avoid when:**
- You want the best inline completion quality (use Cursor or Copilot)
- Your codebase is small or single-repo
- You need agent mode capabilities
- Cost is a primary concern

## Roster entry

- **Name:** Cody
- **Type:** Codebase assistant
- **License:** Proprietary
- **Region:** US
- **Tier:** B
- **Notes:** Sourcegraph; large codebase context; $9–19/mo

---

## Deep Analysis

### 1. How Is This Tool Useful?

Cody's unique strength is deep codebase understanding at scale. While most AI coding assistants are limited to the current file or a few hundred tokens of context, Cody leverages Sourcegraph's code intelligence platform to understand relationships across entire codebases — including multiple repositories. For organizations with millions of lines of code spread across dozens or hundreds of repos, Cody can answer questions like "where is this function used across all our services?" or "what's the data flow from this API endpoint to the database?" — questions that other tools simply cannot answer.

For enterprise engineering organizations, Cody's integration with Sourcegraph's code search and intelligence infrastructure is a natural fit. Teams already using Sourcegraph for code search get AI assistance that understands the same code graph. This means Cody's answers are grounded in actual code relationships, not just approximate semantic search. For onboarding new engineers to large codebases, Cody's ability to explain how systems connect and where to find relevant code is genuinely transformative.

The multi-repository context is Cody's killer feature for large organizations. Most AI assistants work within a single repository or workspace. Cody can search across all repositories in your Sourcegraph instance, making it possible to understand cross-service dependencies, find duplicate implementations across teams, and trace data flows through microservice architectures. For organizations struggling with "I don't know where things are" problems at scale, this is uniquely valuable.

### 2. Gotchas of Using This Tool

Coding assistance quality trails Cursor and Copilot. Cody's strength is codebase understanding (search, explanation, navigation), not inline completion or code generation. Developers who primarily want fast, accurate inline completions or sophisticated code generation will find Cody less capable than alternatives. The tool excels at "explain this codebase" and "where is X used?" but is weaker at "write this function for me."

The best features require Sourcegraph enterprise infrastructure. While Cody Free and Pro work as standalone IDE extensions, the multi-repository context, code graph features, and enterprise governance require a Sourcegraph instance. This means the full value proposition is locked behind enterprise pricing and infrastructure setup. Teams evaluating Cody should understand that the free/pro experience is significantly less capable than the enterprise experience.

The smaller community means fewer resources. Cody has a smaller user base than Copilot or Cursor, which means fewer tutorials, community tips, and third-party integrations. Problem-solving often requires Sourcegraph's official support rather than community knowledge. This isn't necessarily a problem (Sourcegraph's support is generally good), but it's a different experience from the large communities around Copilot and Cursor.

### 3. Limitations

- **Coding assistance quality**: Trails Cursor/Copilot for completion and generation
- **Enterprise dependency**: Best features require Sourcegraph infrastructure
- **No agent mode**: Cannot autonomously execute multi-step tasks
- **Smaller community**: Fewer resources and tutorials
- **Multi-repo locked to enterprise**: Free/Pro limited to single repo
- **Latency**: Code graph queries add response time
- **Setup complexity**: Enterprise deployment requires Sourcegraph expertise

### 4. How Secure Is This Tool?

- **SOC 2 Type II**: Certified (Sourcegraph)
- **GDPR**: Compliant
- **On-premises**: Available with Sourcegraph enterprise — full data control
- **Data handling**: Cloud mode processes code on Sourcegraph servers; enterprise on-prem keeps everything internal
- **Encryption**: TLS in transit, AES-256 at rest
- **Known CVEs**: No major security advisories as of mid-2026
- **Code exfiltration risk**: Low with on-prem; moderate in cloud mode
- **Enterprise**: SSO, SAML, audit logs, custom data retention
- **Public repo snapshot**: [sourcegraph/cody-public-snapshot](https://github.com/sourcegraph/cody-public-snapshot) — 3.8K stars

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 1/10**

Cody is an enterprise developer tool requiring IDE knowledge and, for full value, Sourcegraph infrastructure. Non-technical users cannot use it. The codebase understanding features could theoretically help non-developers understand code relationships, but the interface is developer-focused.

### 6. What Does This Tool Solve That Others Don't?

Cody's unique advantages:

- **Multi-repository code understanding**: Can search and reference code across all repos — unique
- **Sourcegraph code graph**: Grounded in actual code relationships, not just semantic search
- **Enterprise code intelligence**: Leverages mature code search infrastructure
- **Scale**: Best-in-class for very large codebases (millions of LOC, hundreds of repos)
- **On-premises with full features**: Enterprise deployment preserves all capabilities

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Key Advantage | Key Disadvantage |
|------|------|--------------|-----------------|
| 1 | GitHub Copilot | Best all-around; widest adoption | No multi-repo understanding |
| 2 | Cursor | Best IDE; completions | No multi-repo understanding |
| 3 | **Cody** | Multi-repo; code graph; scale | Weaker completions; enterprise dependency |
| 4 | Continue | Open-source; multi-IDE | No code graph |

### 8. How Can This Tool Be Improved? How Active Is Development?

**Development activity**: Active. Sourcegraph is a well-established company. Cody receives regular updates. The public snapshot repo ([sourcegraph/cody-public-snapshot](https://github.com/sourcegraph/cody-public-snapshot)) has 3.8K+ stars; the main product is proprietary.

**Areas for improvement:**
- Inline completion quality to match Copilot/Cursor
- Agent mode for autonomous task execution
- Multi-repo features available at lower tiers (not just enterprise)
- Better standalone experience without Sourcegraph
- More transparent pricing
- Larger community and more tutorials
- Better integration with CI/CD pipelines

### 9. Official Maintainer Contacts

- **Company**: Sourcegraph — https://sourcegraph.com, https://cody.sourcegraph.com
- **GitHub**: [@sourcegraph](https://github.com/sourcegraph) ([cody-public-snapshot](https://github.com/sourcegraph/cody-public-snapshot))
- **Twitter/X**: [@sourcegraph](https://twitter.com/sourcegraph)
- **Discord**: Sourcegraph community Discord
- **Docs**: https://docs.sourcegraph.com/cody
- **Email**: hi@sourcegraph.com, support@sourcegraph.com
- **Community**: community.sourcegraph.com

### 10. General Usage Guidance

**Getting started:**
1. Sign up at cody.sourcegraph.com (free tier available)
2. Install extension for VS Code or JetBrains
3. Authenticate with your Sourcegraph account
4. Start with codebase questions ("explain this function")
5. Try multi-repo search (enterprise tier)
6. Use @mentions to include specific files or symbols

**Best practices:**
- For enterprise: deploy Sourcegraph instance for full code graph
- Use Cody for codebase understanding (its strength), not just completion
- Index all repositories for cross-repo search (enterprise)
- Configure custom models for enterprise (if you have specific model requirements)
- Use alongside a completion-focused tool (Copilot/Cursor) for full coverage
- Leverage Cody for onboarding new team members to large codebases

**When NOT to use:**
- If your codebase is small and single-repo (overkill)
- If inline completion quality is your top priority (use Copilot or Cursor)
- If you need agent mode capabilities (use Cline or Claude Code)
- If you don't want to invest in Sourcegraph infrastructure

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*
