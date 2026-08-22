# Zed Editor Configuration Guide

This document describes the configuration of the Zed editor to enable advanced AI capabilities, including local LLMs via Ollama and specialized MCP (Model Context Protocol) servers for documentation and web research.

## 🛠 Prerequisites

- **Zed Editor** (Latest version)
- **Ollama** installed and running locally (`ollama serve`)
- **Node.js/npm** or **Python** (depending on the MCP server implementation)

## ⚙️ Configuration (`settings.json`)

To apply these settings, open your Zed settings (`cmd+,`) and ensure your `settings.json` includes the following blocks.

### 1. Local LLM via Ollama

To use Ollama as a local language model provider, configure the `language_models` section. This allows Zed to use models like `llama3` or `mistral` running on your machine.

```json
{
  "language_models": {
    "ollama": {
      "api_url": "http://localhost:11434"
    }
  }
}
```

### 2. MCP Servers (Context7 & Tavily)

The Model Context Protocol (MCP) allows Zed to connect to external tools. We use two specific servers:
- **Context7**: For retrieving up-to-date library documentation and code examples.
- **Tavily**: For real-time web search and research.

Add this to your `mcp` configuration:

```json
{
  "mcp": {
    "servers": {
      "tavily": {
        "command": "npx",
        "args": ["-y", "@tavily/mcp-server"],
        "env": {
          "TAVILY_API_KEY": "YOUR_TAVILY_API_KEY_HERE"
        }
      },
      "context7": {
        "command": "npx", 
        "args": ["-y", "@context7/mcp-server"]
      }
    }
  }
}
```

> [!IMPORTANT]
> Replace `YOUR_TAVILY_API_KEY_HERE` with your actual API key from [tavily.com](https://tavly.com).

## 🔍 Verifying the Setup

### Check Ollama
1. Open the Zed Assistant Panel (`cmd+shift+a`).
2. Select an **Ollama** model from the model dropdown.
3. Type a simple prompt (e.g., "Hello"). If it responds, Ollama is connected.

### Check MCP Servers
1. Open the Zed Assistant Panel.
2. Look for the **Tools** or **Context** indicators.
3. You can trigger a search by asking: *"Search the web using Tavily for the latest Flask news"* or *"Use Context7 to find documentation for Flask routing"*.
4. If the tool calls appear in the assistant's thought process/logs, the MCP servers are active.

## 🚀 Summary of Capabilities
| Tool | Purpose | Capability |
| :--- | :--- | :--- |
| **Ollama** | Local Intelligence | Code generation, refactoring, and logic analysis without cloud latency or cost. |
| **Context7** | Deep Library Knowledge | Instant access to accurate, structured documentation for Python frameworks and libraries. |
| **Tavily** | Real-time Research | Web-wide search to find recent ecosystem updates, tutorials, and troubleshooting guides. |

Example of using them together. A good research prompt for your Zed Agent would be:

```


Use Context7 and Tavily to research the best current Python development setup for this Flask repository on macOS.

Start by inspecting this repository to understand the existing Flask version, dependencies, project structure, deployment assumptions, and any existing Python-version configuration.

Then research current official documentation and current best practices.

Compare at least:

system/Homebrew Python + venv
pyenv + venv
uv

Determine:

Which Python version we should standardize on.
How Python itself should be installed and version-pinned.
How the project's virtual environment should be managed.
How dependencies should be declared and locked.
Whether we should use requirements.txt or pyproject.toml.
What files should be committed versus added to .gitignore.
How Zed should discover the correct Python interpreter.
Whether the setup will work cleanly in CI and production.

Prefer official Flask and Python documentation through Context7. Use Tavily for recent ecosystem/tooling comparisons.

Do not change anything yet. Give me a recommended setup, explain the tradeoffs, and provide the exact commands you would run.
```
