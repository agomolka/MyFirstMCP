# Architecture

`first-mcp-insights` is a small Model Context Protocol server for learning how LLMs interact with external tools.

## Flow

```text
User
  ↓
LLM Client
  ↓
MCP Client
  ↓
first-mcp-insights MCP Server
  ↓
Python tools
  ↓
pandas + local CSV datasets