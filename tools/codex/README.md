# <Tool name>

## 1. What it is

Codex is OpenAI's AI coding helper. I used the Codex extension inside VS Code. It has a side panel where I type tasks and it shows its plan, its file changes and its answers.

## 2. Cost and access

I did not buy any plan or credits. Access I used:  "a free ChatGPT account". Model shown in the panel: 5.6 Tera Extension publisher: OpenAI. Extension version: 26.917.62051.
## 3. How I installed and ran it
VS Code, Extensions (Ctrl+Shift+X), search "Codex", check that the publisher is OpenAI, Install.
Signed in through the browser. I did not choose the API key option.
In the terminal, I made a clean branch for this tool:
git switch master
git switch -c codex
I copied the rules file and added the venv Python line:
cp AGENTS.md.example AGENTS.md
echo "- Run tests with: ./.venv/Scripts/python.exe -m pytest -q" >> AGENTS.m
## 4. How it understands the codebase
I asked for a read-only summary and checked it against the code.
- Files listed: README.md, cart.py, pricing.py, cli.py, both test
  files, requirements.txt.
- Entry point: correct (python -m shopcart.cli).
- Flow: correct (Cart, add_item, apply_coupon, subtotal, total).
- Data shape: correct (items is {sku: {"price", "qty"}}).
- Quantity bug: not mentioned, because I did not ask for bugs.
- Made-up claims: none found.
- Gaps: it skipped __init__.py and AGENTS.md.
## 5. Customization support
| Feature | Supported / Unsupported / Untested | Notes |
|---|---|---|
| Project instructions (AGENTS.md etc.) |tested |It followed the test command and the type hint rule |
| Skills | | |
| Plugins/extensions |it is a extension |untested |
| MCP | | |

## 6. Practical task
Task 1: add clear()
Its plan: inspect Cart, add clear() that empties the items and resets the coupon, put the tests in a new file, run the tests, leave the add_item bug alone.
I approved the plan and added: give the tests "-> None" type hints.
Result: it created tests/test_cart_clear.py with 2 tests (clear the items, reset the coupon).
It said cart.py needed no change because clear() already existed. This was true, but not because of the baseline: my folder had an unsaved clear() edit, probably from an earlier Codex attempt that gave errors. Codex told me instead of overwriting it.
I was on the master branch by mistake. I switched to the codex branch before committing, so master stayed clean.
Tests after this step: 7 passed, 1 failed (the known bug)

Task 2: fix the bug
Prompt: diagnose why test_adding_same_sku_increases_quantity fails, explain first, then fix, and wait for my approval.
Cause it found: add_item always replaced the item, so quantity 2 was overwritten by 3 instead of adding up to 5.
Fix: if the item exists, add to its quantity and use the latest price. New items are created as before. The qty <= 0 check stays.
Files: shopcart/cart.py only. No test was changed.
Time: "Worked for 13s"

Tests
Stage	Passed	Failed
Before (baseline)	5	1
After clear()	7	1
After bug fix 8     -


Demo program: Subtotal 9.50 before, after 15.50. Total 8.55 before,  after  13.95.

Did it follow AGENTS.md?

Type hints: yes (-> None on clear() and the new tests).
Old tests untouched: yes.
Test command with the venv Python: ___

## 7. Permissions and approvals
for both tasks it wrote a plan in the chat and waited for my approval before editing ("Waiting for your approval"). I checked each plan against my rules and then approved it. I did not reject anything.

## 8. Worked / failed / manual corrections
Worked:
Clear plan and a clear root cause before editing.
It waited for my approval.
It reported honestly that clear() already existed.
Very fast: the bug fix took 13 seconds.
Problems:
It wrote only 2 tests, where OpenCode and Cline wrote 4.

## 9. Best use, limits, recommendation
Best use: quick, small, clear tasks where I want a plan first and a
fast result. The bug fix took only 13 seconds, and it waited for my
approval before editing. It also told me honestly when something did
not match (clear() already existed) instead of overwriting it.

Limits:
- Its final summary was short 
- It wrote fewer tests than OpenCode and Cline (2 instead of 4).
- I only tested a very small project, so I cannot say how it works on
  a large one.

Recommendation: I would recommend Codex to people who want fast,
careful help on small tasks, as long as they check the results
themselves. It is a good choice for daily small fixes. For big or
risky work I would want more testing first.
