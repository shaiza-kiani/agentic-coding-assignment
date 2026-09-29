from shopcart.cart import Cart


def test_clear_removes_all_items():
    c = Cart()
    c.add_item("pen", 1.50, 2)
    c.add_item("book", 10.00, 1)
    c.clear()
    assert c.items == {}
    assert c.subtotal() == 0.00


def test_clear_resets_discount():
    c = Cart()
    c.add_item("book", 10.00, 1)
    c.apply_coupon("save10")
    c.clear()
    assert c.discount_percent == 0
    assert c.total() == 0.00


def test_clear_on_empty_cart_is_noop():
    Cart().clear()


def test_cart_is_usable_after_clear():
    c = Cart()
    c.add_item("pen", 1.50, 2)
    c.clear()
    c.add_item("book", 10.00, 1)
    assert c.items["book"]["qty"] == 1
    assert c.subtotal() == 10.00
