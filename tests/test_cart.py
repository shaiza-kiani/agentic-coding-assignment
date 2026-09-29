import pytest
from shopcart.cart import Cart


def test_subtotal_single_item():
    c = Cart()
    c.add_item("pen", 1.50, 2)
    assert c.subtotal() == 3.00


def test_adding_same_sku_increases_quantity():
    c = Cart()
    c.add_item("pen", 1.50, 2)
    c.add_item("pen", 1.50, 3)
    assert c.items["pen"]["qty"] == 5


def test_coupon_reduces_total():
    c = Cart()
    c.add_item("book", 10.00, 1)
    c.apply_coupon("save10")
    assert c.total() == 9.00


def test_invalid_qty_rejected():
    c = Cart()
    with pytest.raises(ValueError):
        c.add_item("pen", 1.50, 0)
