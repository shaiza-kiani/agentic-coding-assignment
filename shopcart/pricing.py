"""Pricing helpers for the shopping cart."""

COUPONS = {"SAVE10": 10, "SAVE20": 20}  # percent off


def apply_percent_discount(amount: float, percent: float) -> float:
    """Return amount after a percentage discount."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(amount * (1 - percent / 100), 2)


def coupon_percent(code: str) -> float:
    """Look up a coupon code. Unknown codes raise KeyError."""
    return COUPONS[code.upper()]
