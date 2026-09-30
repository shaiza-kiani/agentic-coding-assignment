# Agentic Coding Platforms: Submission (Sajil Tariq)

## Purpose
I tested free AI coding agents on one small shared project (shopcart, a
shopping cart in Python). Every tool got the same tasks: understand the repo,
follow an AGENTS.md file, add a clear() method, and fix a quantity bug.
I checked every result myself with git and pytest.

## Demo codebase
- Folder: [demo-codebase/](demo-codebase/)
- GitHub: https://github.com/shaiza-kiani/agentic-coding-assignment
- Branches: master (baseline with the bug), opencode, cline, pi, codex, extra

## Tool reports
| Tool | Status | Report |
|---|---|---|
| OpenCode | Tested (full workflow) | [tools/opencode](tools/opencode/README.md) |
| Cline | Tested (full workflow) | [tools/cline](tools/cline/README.md) |
| Pi Coding Agent | Partly tested (setup, understand, plan; edits failed) | [tools/pi](tools/pi/README.md) |
| Additional free tool: ____ | ___ | [tools/additional-free-tool](tools/additional-free-tool/README.md) |
| OpenAI Codex | Tested (full workflow) | [tools/codex](tools/codex/README.md) |
| Google Antigravity | only downloaded extension | [tools/antigravity](tools/antigravity/README.md) |

## Other files
- [Comparison table](comparison.md)
- Concepts: [skills](concepts/skills.md), [plugins and extensions](concepts/plugins-and-extensions.md), [MCP](concepts/mcp.md), [project instructions](concepts/project-instructions.md)
- Evidence (screenshots and logs): [evidence/](evidence/)

## Conclusion
- Cline gave the most control and the clearest plans, so it fits daily work
  in VS Code.
- OpenCode is free and asks questions before it edits, so it suits beginners
  and terminal users.
- Codex was the fastest for small fixes.
- Pi did not work well with the free models I could use. That is not a fair
  verdict on Pi with a strong model.
- Main lesson: agents help, but I always read the diff and run the tests
  myself. One tool ignored a "do not edit" instruction once.

## Tools not fully tested, and why
- Pi: Copilot Free gave "model not supported" on every model. The OpenRouter
  free models hit rate limits (429) and failed during file edits
  (finish_reason: error). So I could not finish the Change and Debug steps.
- Google Antigravity: downloaded and it read my files then asks permisiion but i was not sure if i was doing it write
- Skills, plugins and MCP were not tested on the tools I used

## Notes
- No paid plans, credits or payment details were used.
- No secrets are in the repo. .env and .venv are in .gitignore.