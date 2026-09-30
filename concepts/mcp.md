# MCP
MCP (Model Context Protocol) is a standard way to connect an AI agent to
outside tools and data, like files, GitHub or a database.
An MCP server offers a list of tools, such as "read a file" or "list a
folder". 
Difference from the others: AGENTS.md is rules for one project, skills are
saved instructions, plugins add features, and MCP connects to outside tools.
## Security risks
- Too much access: a server given my whole drive could read secrets.
- Actions that change things: some servers can write or delete files.
- Untrusted servers: an unknown server can be harmful.
- Prompt injection: a file the agent reads can hide instructions that trick it.
- Leaked API keys.
## How I stayed safe
I did not test an MCP server. In my tool tests I rejected requests outside
my project, never used auto-approve, read every command and diff, and kept
.env and keys out of Git.
.
