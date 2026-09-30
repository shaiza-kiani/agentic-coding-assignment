# <OpenCode>

## 1. What it is
OpenCode is an AI coding agent that runs in the terminal. I used it inside VS Code. It has two modes:
Build: it can change files.
Plan: it can only read.

## 2. Cost and access
The tool is free. I did not pay or use any API key.I used a free model called Big Pickle.
## 3. Install and run (reproducible)
node --version v20.20.2,
 npm i -g opencode-ai@latest,
opencode --version 1.18.33,
opencode

## 4. How it understands the codebase
I asked it to inspect the repo without editing. It ran a shell
command (ls -la) to list the files, then read them. 
I did not see a search index. It seems to explore with commands each
time, but I am not sure how it works inside.
Right: entry point (cli.py), how Cart uses pricing.py, the quantity
bug, missing clear(), raw KeyError.
Made-up claims: none found.
Note: my code had a "BUG (planted)" comment, which may have helped it.

## 5. Customization support
| Feature | Status | Notes |
|---|---|---|
| Project instructions (AGENTS.md) | Tested | It followed my rules: type hints, old tests untouched |
| Skills | Untested | I have not tried this yet |
| Plugins/extensions | Untested | I have not tried this yet |
| MCP | Untested | I have not tried this yet |

## 6. Practical task
Task 1: add clear()
- Prompt: "Add a clear() method to Cart with a test. Show me your plan
  first and do not edit anything until I approve."
- Result: clear() empties the cart and removes the coupon (my choice).
  4 new tests in tests/test_cart_clear.py.
- Files: cart.py (edited), test_cart_clear.py (new), AGENTS.md (new)
- Commit: 6ede91b

Task 2: fix the bug
- Prompt: "Diagnose why test_adding_same_sku_increases_quantity fails.
  Explain the cause first, then show me the fix and wait for my approval."
- Cause: add_item replaced the old entry, so the old quantity was lost.
- Fix: it now adds to the quantity and updates the price (my choice).
- Files: cart.py
- Commit: 1558274

Tests
| Stage | Passed | Failed |
|---|---|---|
| Before (baseline) | 5 | 1 |
| After clear() | 9 | 1 |
| After bug fix | ___ | ___ |

Demo program subtotal: 9.50 before, ___ after.

Did it follow AGENTS.md?
- Type hints: yes (-> None on add_item)
- Old tests untouched: yes
- Ran pytest: ___ (yes/no)

Evidence: 

## 7. Permissions and approvals
It asked to access a folder outside my project. I chose Reject and
  told it to stay inside the folder.It asked me design questions before editing (reset coupon or not, where to put tests, which price to keep). I answered each one. Options were Allow once, Allow always and Reject. I never used
  Allow always.

## 8. Worked / failed / manual corrections

Worked:
- It asked questions before editing instead of guessing.
- It stayed on the task and left the old tests alone.
- It followed my AGENTS.md rules.

Failed or was a problem:
- It was slow. The first task took about 19 minutes.

- I started in Build mode when I meant to use Plan mode.

What I fixed by hand:

- I deleted a stray folder named {shopcart,tests}.

## 9. Best use, limits, recommendation

Best use: small, clear tasks where I want to review each change.
Plan mode is good for safe read-only questions.

Limits: slow with the free model, and it needs me to answer
questions and read every permission request.

Recommendation: I would recommend it to beginners and for small
projects, because it is free and asks before it acts. For large
projects I would need to test it more.