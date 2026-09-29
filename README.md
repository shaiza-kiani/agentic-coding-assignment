# shopcart (demo codebase)

Tiny in-memory shopping cart used to compare coding agents.
Contains NO secrets and NO real company data.

Setup:     `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
Run tests: `python -m pytest -q`
Run demo:  `python -m shopcart.cli`

## Agent tasks (same for every tool)
- **Feature:** add a `clear()` method to `Cart` plus a test.
- **Bug:** `test_adding_same_sku_increases_quantity` fails. Diagnose and fix.
- **Refactor (optional):** raise a friendly `InvalidCouponError` for unknown coupon codes.
