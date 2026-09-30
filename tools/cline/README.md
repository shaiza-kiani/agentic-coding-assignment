# <Cline>

## 1. What it is
Cline is an AI coding helper that lives inside VS Code as an
extension. It has a side panel with two modes:
 Plan: it only reads and makes a plan.
  Act: it can edit files and run commands, after I approve.


## 2. Cost and access
The extension is free. I signed in with a free account and picked a
model tagged FREE:Deepseek v4.1-Flash.

## 3. Install and run (reproducible)
1. VS Code, Extensions (Ctrl+Shift+X), search "Cline", Install.
2. Signed in through the browser (free account).
3. Set the provider to Cline and chose a FREE model.
4. Used the terminal: git switch cline
Version:4.1.21

## 4. How it understands the codebase
It listed the files with commands (git ls-files, dir, ls), skipped
.venv, and read the source files. It also checked for hidden config
files and read my AGENTS.md before planning.

## 5. Customization support
| Feature | Status | Notes |
|---|---|---|
| Project instructions (AGENTS.md) | Tested | It quoted my rules and followed them |
| Skills | Untested | |
| Plugins/extensions | It is an extension itself | Other add-ons untested |
| MCP | Untested | |

## 6. Practical task
Task 1: add clear()
- Prompt: "Add a clear() method to Cart with a test. Show me your
  plan first. Follow AGENTS.md."
- Result: clear() empties the cart and removes the coupon. 4 new tests
  in tests/test_cart_clear.py.
- Files: cart.py (edited), test_cart_clear.py (new), AGENTS.md (new)
- Commit: Cline: add Cart.clear() with tests (hash: ___)

Task 2: fix the bug
- Prompt: "Diagnose why test_adding_same_sku_increases_quantity fails.
  Explain the root cause first, then show me your proposed fix and
  wait for my approval."
- Cause: add_item replaced the old entry, so the old quantity was lost.
- Fix: adds to the quantity and updates the price (my choice).
- Files: cart.py only
- Commit: f03649f
- Tests:
| Stage | Passed | Failed |
|---|---|---|
| Before | 5 | 1 |
| After clear() | 9 | 1 |
| After fix | 10 | 0 |

Demo: Subtotal 9.50 before, 15.50 after. Total 8.55 before, 13.95 after.
Did it follow AGENTS.md? Type hints: ___. Old tests untouched: yes.
Used the venv Python from my extra rule: yes.

Evidence: evidence/cline-afterfix2.png
## 7. Permissions and approvals
Every command needed my click (Approve or Reject).
I rejected one command that listed folders outside my project.
I did not turn on auto-approve.
It asked design questions (test file location, which price to keep)and I answered them.

## 8. Worked / failed / manual corrections
Worked:
- Detailed plan before editing.
- It proved the bug with a live experiment before fixing.
- It caught its own wrong expected number (4.0/3.2 instead of 5.0/4.0).

Problems:
- Many approval steps and side-checks (for example line endings).
- Its terminal used system Python, not my .venv, so pytest was missing
  at first. It fixed this itself.

My corrections:
- I rejected the outside-folder command.
- I told it to leave the line-ending file alone and stay on the bug.

## 9. Best use, limits, recommendation
Best use: work inside VS Code where I want to see a plan, review
each change, and approve each command. It is good for careful
tasks like bug fixing, because it tests its ideas before editing.

Limits:
- It asks for approval many times, so it feels slow.
- It did side-checks I did not ask for (like line endings).
- It needed a free model, and its terminal did not use my .venv at first.
- I only tested it on a very small project.

Recommendation: I would recommend Cline to beginners and to people
who like a visual panel in VS Code, because it shows every plan,
diff and command before acting.