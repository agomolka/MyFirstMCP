# First MCP Insights

My first Model Context Protocol server for exploring datasets with LLMs using Python, pandas, and MCP.

## Why this project?

This project is a beginner-friendly MCP server designed for AI engineers and data scientists who want to understand how LLMs can use external tools.

The server lets an MCP-compatible LLM client inspect and analyze a local CSV dataset.

## What it does

`first-mcp-insights` exposes data science tools to an LLM client:
- List available datasets
- Profile a dataset
- Inspect numeric and categorical columns
- Preview rows
- Generate summary statistics
- Compute Pearson correlation
- Filter rows
- Count values in a column

## Architecture

```text
User
  ↓
LLM Client
  ↓
MCP Client
  ↓
first-mcp-insights MCP Server
  ↓
pandas + local CSV
```

## Test the server with MCP Inspector
npx @modelcontextprotocol/inspector first-mcp-insights

## Security notes
This project is intentionally limited for safety:
* It only reads CSV files.
* It only reads files from the local data/ directory.
* It does not execute arbitrary code.
* It does not run SQL.
* It limits preview sizes.
