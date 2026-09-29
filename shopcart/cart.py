"""A tiny in-memory shopping cart."""
from shopcart.pricing import apply_percent_discount, coupon_percent


class Cart:
    def __init__(self):
        self.items = {}  # sku -> {"price": float, "qty": int}
        self.discount_percent = 0

    def add_item(self, sku: str, price: float, qty: int = 1) -> None:
        if qty <= 0:
            raise ValueError("qty must be positive")
        existing = self.items.get(sku)
        if existing is None:
            self.items[sku] = {"price": price, "qty": qty}
        else:
            existing["price"] = price
            existing["qty"] += qty

    def remove_item(self, sku: str):
        del self.items[sku]

    def clear(self) -> None:
        """Remove all items from the cart and reset the applied discount."""
        self.items.clear()
        self.discount_percent = 0

    def subtotal(self) -> float:
        return round(sum(i["price"] * i["qty"] for i in self.items.values()), 2)

    def apply_coupon(self, code: str):
        self.discount_percent = coupon_percent(code)

    def total(self) -> float:
        return apply_percent_discount(self.subtotal(), self.discount_percent)
