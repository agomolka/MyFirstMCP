# First MCP Insights

My first Model Context Protocol server for exploring datasets with LLMs using Python, pandas, and MCP.

## Why this project?

This project is a beginner-friendly MCP server designed for AI engineers and data scientists who want to understand how LLMs can use external tools.

The server lets an MCP-compatible LLM client inspect and analyze a local CSV dataset.

## What it does

`MyFirstMCP` exposes data science tools to an LLM client:
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
MyFirstMCP
  ↓
pandas + local CSV
```

## Test the server with MCP Inspector
npx @modelcontextprotocol/inspector MyFirstMCP

## Security notes
This project is intentionally limited for safety:
* It only reads CSV files.
* It only reads files from the local data/ directory.
* It does not execute arbitrary code.
* It does not run SQL.
* It limits preview sizes.
