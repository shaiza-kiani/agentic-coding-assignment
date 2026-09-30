# Comparison

Same small project (shopcart) and same tasks for every tool: understand the
repo, add clear(), fix the quantity bug. Ratings are 1 to 5 (5 is best),
based only on my own tests.

| Criterion | OpenCode | Pi | Cline | Codex | Extra: ____ |
|---|---|---|---|---|---|
| Access & setup | 4/5 - Free tool, free model (Big Pickle), no key.. | 2/5 - Copilot Free login worked, but every model gave model_not_supported. Needed an OpenRouter free key. Hit rate limits (429). | 4/5 - Free extension, free account, FREE model. Smooth in VS Code. | 3/5 -  Access route: ___ | Not tested yet |
| Codebase understanding | 4/5 - Right entry point, flow, bug, missing clear(). Nothing invented. | 3/5 - Accurate with a working model. Early path errors and it listed .venv files. | 4/5 - Read AGENTS.md first, accurate. Used a leftover cache as a hint. | 4/5 - Accurate entry point and flow. Short, and did not mention the bug (I did not ask). | Not tested yet |
| Planning & edits | 4/5 - Asked design questions first. Focused diff, followed AGENTS.md. | 2/5 - One run ignored "do not edit" and changed 3 files, including an old test. Later edits failed twice (finish_reason: error). | 5/5 - Most detailed plan. Small focused fix (3 lines added, 2 removed). | 4/5 - Clear plan and correct root cause. Wrote only 2 tests. | Not tested yet |
| Terminal & VS Code | 3/5 - Text screen in the VS Code terminal. Tried to read outside the project. | 3/5 - Text screen in the terminal. Ran commands by itself. Downloaded helper tools on first start. | 4/5 - Panel with Plan and Act modes. Wrong shell commands and Python at first, then fixed itself. | 4/5 - Panel in VS Code. Sandbox blocked pytest cache writes. | Not tested yet |
| Tests & debugging | 4/5 - Explained the cause, fixed it, reported results correctly. | 1/5 - Did not finish the change or the fix with any free model. | 5/5 - Proved the bug with a live experiment. Caught its own wrong expected number. | 4/5 - Correct cause and fix in 13 seconds. Summary had no test results, so I ran them. | Not tested yet |
| Customization | 3/5 - AGENTS.md followed. Skills, plugins, MCP untested. | 2/5 - Read AGENTS.md when planning. The rest untested. | 3/5 - AGENTS.md followed. MCP untested. | 3/5 - AGENTS.md followed. The rest untested. | Not tested yet |
| Safety & control | 4/5 - Allow once, Allow always or Reject. I rejected an outside-folder request. | 1/5 - I saw no approval step. It ran commands and edits by itself and once ignored a read-only rule. | 5/5 - Every command needed my click. I rejected an outside-folder command. Auto-approve off. | 4/5 - Waited for my approval of each plan. Sandbox limited writes. I ran git myself. | Not tested yet |
| Overall fit | Beginners and terminal users. Free and careful, but slow (about 19 min for the first task, including my reading time). | Not a fit with free models. Not a fair verdict on Pi with a strong model. | Daily work in VS Code. Most control, but many approval steps. | Quick, small tasks. Fast, but check the results yourself. | Not tested yet |

Notes on fairness:
- Each tool used a different model, so speed and quality partly reflect the model.
- Cline found a leftover .pytest_cache from an earlier tool, a small head start.
- Codex started with an unsaved clear() edit in my folder, so its task was smaller.
- My "BUG (planted)" comment may have helped the tools find the bug.
- Skills, plugins and MCP were not tested, so Customization ratings are limited.


## Team recommendation
Beginners: OpenCode. It is free, works without a key, and asks questions
before it edits.

Daily work: Cline. It gave the most control, the clearest plans and the
safest approvals. It is slower because of the approval steps, but a team
that reviews every change will accept that.

Quick small fixes: Codex. It was the fastest. Check its results yourself.

Large repositories: I did not test any tool on a large repo, so I cannot
recommend one. I would test Cline or Codex on a bigger project first.

I would not use Pi with free models. It ignored a read-only instruction
once, showed no approval step, and its edits failed. This is about the free
models I could use, not a final verdict on Pi.

For every tool: keep an AGENTS.md file, do not turn on auto-approve, read
every diff and command, use one fixed model, and run the tests yourself.
