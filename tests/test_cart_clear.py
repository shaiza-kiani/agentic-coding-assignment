"""Tests for clearing a shopping cart."""
from shopcart.cart import Cart


def test_clear_empties_items() -> None:
    cart = Cart()
    cart.add_item("pen", 1.50, 2)

    cart.clear()

    assert cart.items == {}


def test_clear_resets_coupon() -> None:
    cart = Cart()
    cart.apply_coupon("SAVE10")

    cart.clear()

    assert cart.discount_percent == 0
