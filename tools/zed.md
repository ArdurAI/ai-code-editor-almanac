# Zed


[![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

| Attribute | Value |
|-----------|-------|
| Tier | A |
| Type | Rust-native editor |
| License | Open source (GPL/AGPL core + proprietary extensions) |
| Region | Global |
| URL | https://zed.dev |

## One-line summary

86K+ GitHub stars; GPU-accelerated Rust-native code editor with multi-provider AI chat, real-time collaboration, and industry-leading performance.

## Architecture

Zed is a high-performance code editor built in Rust by the creators of Atom and Tree-sitter. Key architectural elements:

- **Rust-native**: Built from scratch in Rust for maximum performance; GPU-accelerated rendering
- **GPUI framework**: Custom GPU-based UI framework for 120fps+ rendering
- **Multi-provider AI**: Built-in AI assistant supporting Claude, GPT, Gemini, and custom endpoints
- **Real-time collaboration**: Built-in CRDT-based collaborative editing (no extension needed)
- **Language Server Protocol**: Full LSP support for intelligent code completion and navigation
- **Tree-sitter integration**: Native tree-sitter support for fast syntax highlighting and code understanding
- **Editor + Terminal**: Integrated terminal within the editor

## Key features

- Industry-leading performance (GPU-accelerated; 120fps+ rendering)
- Built-in AI assistant panel (multi-provider: Claude, GPT, Gemini)
- Real-time collaboration (CRDT-based; built-in)
- Full LSP support (completion, diagnostics, navigation)
- Rust-native (low memory footprint; fast startup)
- Integrated terminal
- Vim mode (first-class)
- Extension system (growing ecosystem)
- macOS native; Linux and Windows support in development
- Open source core (GPL/AGPL)

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Not applicable | Editor performance, not coding accuracy |
| Latency | Industry-leading | Fastest editor rendering; sub-millisecond input |
| Token economics | Not run | AI features are BYOK or via Zed's subscription |
| Scale behavior | Strong | Handles large files and projects efficiently |
| Ops burden | Low | Single download; minimal config |
| Developer experience | Very high | Best-in-class performance and polish |
| Data sovereignty | Partial | BYOK for AI; collaboration via Zed's servers |

## Ops reality

**Setup burden:** Low — download from zed.dev; minimal configuration.

**Sharp edges:**
- AI features are less mature than dedicated AI IDEs (Cursor, Copilot)
- Extension ecosystem is smaller than VS Code's
- macOS-first; Linux/Windows support still maturing
- Collaboration features require Zed account
- No inline AI completion (chat-only AI integration)

## Cost model

| Plan | Price | Key features |
|------|-------|-------------|
| Free (Open Source) | $0 | Full editor; local AI with BYOK |
| Zed Pro | ~$10/mo | Enhanced AI; collaboration features |
| AI BYOK | API costs | Use your own Claude/GPT/Gemini API keys |

## When to use / when to avoid

**Use when:**
- Performance and responsiveness are your top priorities
- You want real-time collaboration built into the editor
- You use macOS primarily
- You want a lightweight, fast alternative to VS Code

**Avoid when:**
- You need deep AI integration (inline completion, agent mode) — use Cursor
- You depend on the VS Code extension ecosystem
- You primarily use Windows or Linux
- You need enterprise management features

## Roster entry

- **Name:** Zed
- **Type:** Rust-native editor
- **License:** Open source (GPL/AGPL core)
- **Region:** Global
- **Tier:** A
- **Notes:** Multi-provider chat; real-time collab; GPU-accelerated

---

## Deep Analysis

### Daily monitoring update — 2026-07-10

- **Latest release:** `v1.10.1` (2026-07-09): adds OpenAI-provider support for GPT 5.6 Sol/Terra/Luna and fixes CLI workspace restoration when `cli_default_open_behavior: new_window` is set and no path is provided.

### Daily monitoring update — 2026-07-09

- **Latest release:** `v1.10.0` (2026-07-08): adds llama.cpp as a language-model provider, adds a `git.inline_blame.location` setting, disables format-on-save by default, moves LLM providers/external agents/MCP servers into the settings editor, and includes agent/UI bug fixes.

### 1. How Is This Tool Useful?

Zed's primary value is raw performance. Built in Rust with a custom GPU-accelerated rendering framework (GPUI), Zed delivers an editing experience that feels instant — sub-millisecond input latency, 120fps+ rendering, and the ability to open multi-gigabyte files without hesitation. For developers who've felt the sluggishness of Electron-based editors (VS Code, Cursor), Zed is a revelation. The performance isn't just about speed; it's about flow — when the editor never gets in your way, you stay in the zone.

The built-in real-time collaboration is a standout feature. Unlike VS Code Live Share (which requires an extension and Microsoft account), Zed's collaboration is built into the editor core using CRDTs (conflict-free replicated data types). You can share a project with a teammate and both edit simultaneously with zero configuration — just click "share." For pair programming, code reviews, and remote team collaboration, this is the most seamless experience available. The AI assistant panel provides multi-provider chat (Claude, GPT, Gemini) directly in the editor, though it's currently chat-only without inline completions.

Zed is created by the team behind Atom (GitHub's original editor) and Tree-sitter, bringing deep expertise in editor development. The result is a thoughtfully designed editor that learns from VS Code's UX while abandoning its Electron/Node.js foundation for native Rust. For developers who value craftsmanship, speed, and a focused editing experience, Zed represents the state of the art in editor engineering.

### 2. Gotchas of Using This Tool

AI features are less mature than dedicated AI IDEs. Zed's built-in AI assistant is a chat panel — it doesn't have inline completions (like Copilot or Cursor Tab), agent mode, or deep codebase indexing. If AI is your primary criterion, Cursor, Copilot, or Continue offer more integrated experiences. Zed is a performance-first editor that happens to have AI features, not an AI-first editor.

The extension ecosystem is much smaller than VS Code's. While Zed has an extension system and the library is growing, it can't match VS Code's decades of community extensions. Developers who rely on specific VS Code extensions (particularly niche ones) may find Zed lacking. The gap is closing, but it remains a significant consideration.

macOS-first development. While Zed has been expanding to Linux and Windows, the macOS experience is the most polished. Linux support has improved significantly, but Windows users still face a less mature experience. Teams with mixed operating systems should verify that all members have a good experience on their platform.

### 3. Limitations

- **AI depth**: Chat-only AI; no inline completions or agent mode
- **Extension ecosystem**: Much smaller than VS Code
- **Platform maturity**: macOS-first; Linux/Windows improving but less polished
- **No built-in terminal integration with AI**: Unlike Cursor or Cline
- **Collaboration requires Zed account**: Can't self-host collaboration
- **Learning curve**: Different keybindings and UX from VS Code (though Vim mode is first-class)

### 4. How Secure Is This Tool?

- **License**: Open source (GPL/AGPL core); auditable
- **BYOK for AI**: Your code goes to your chosen provider, not Zed's servers
- **Collaboration**: Uses Zed's servers for real-time sync; data encrypted in transit
- **Telemetry**: Minimal; can be disabled
- **Local-first**: Editor works fully offline; AI requires internet
- **Known CVEs**: No major security advisories as of mid-2026
- **Code exfiltration risk**: Low with BYOK; collaboration sessions involve sharing with participants
- **Enterprise**: Limited enterprise features; collaboration server not self-hostable

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 1/10**

Zed is a professional developer tool. While its performance and polish are excellent, it requires development knowledge to use effectively. The Vim-first design philosophy may appeal to power users but adds a learning curve for newcomers.

### 6. What Does This Tool Solve That Others Don't?

Zed's unique advantages:

- **Unmatched performance**: GPU-accelerated, Rust-native — no editor is faster
- **Built-in collaboration**: CRDT-based real-time editing with zero setup
- **Craftsmanship**: Thoughtfully designed by Atom/Tree-sitter creators
- **Low resource usage**: Minimal memory footprint compared to Electron editors
- **Open core**: Core editor is open source; community can contribute

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Key Advantage | Key Disadvantage |
|------|------|--------------|-----------------|
| 1 | VS Code/Cursor | Largest ecosystem; deepest AI | Electron-based; slower |
| 2 | **Zed** | Fastest; built-in collab; Rust | Smaller ecosystem; macOS-first |
| 3 | Neovim | Maximum customization; terminal | Steep learning curve |
| 4 | JetBrains | Full-featured IDEs per language | Heavy; expensive |

### 8. How Can This Tool Be Improved? How Active Is Development?

**Development activity**: Extremely active. [zed-industries/zed](https://github.com/zed-industries/zed) has **86,367 stars**, 9,346 forks, 3,446 open issues. Last pushed: July 2, 2026. Created February 2021. One of the most active open-source editor projects.

**Areas for improvement:**
- Inline AI completions (the biggest gap vs Cursor/Copilot)
- Extension ecosystem growth (attract VS Code extension developers)
- Full Linux and Windows parity with macOS
- Deeper AI integration (agent mode, codebase indexing)
- Enterprise features (SSO, self-hosted collaboration)
- Better documentation for extension development

### 9. Official Maintainer Contacts

- **Company**: Zed Industries — https://zed.dev
- **GitHub**: [zed-industries/zed](https://github.com/zed-industries/zed) — 86K+ stars
- **Discord**: Zed Community Discord (link in GitHub README)
- **Twitter/X**: [@zeddotdev](https://twitter.com/zeddotdev)
- **Docs**: https://zed.dev/docs
- **Email**: hi@zed.dev

### 10. General Usage Guidance

**Getting started:**
1. Download from zed.dev (macOS, Linux, or Windows)
2. Open a project folder
3. Configure keybindings if needed (VS Code and Vim presets available)
4. Try the AI assistant panel (Cmd+? or configure in settings)
5. Try collaboration: click the share button to invite teammates
6. Browse extensions via the extension manager

**Best practices:**
- Learn the Zed-specific keybindings for maximum efficiency
- Configure AI provider keys for the assistant panel
- Use built-in collaboration for pair programming
- Enable Vim mode if you're a Vim user (first-class support)
- Contribute to the extension ecosystem if you miss a VS Code extension
- Report performance issues — the team is very responsive

**When NOT to use:**
- If AI is your primary feature requirement (use Cursor or Copilot)
- If you depend on specific VS Code extensions not yet available on Zed
- If you need Windows support and it's not yet stable enough for your workflow
- If you need enterprise management features

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*
