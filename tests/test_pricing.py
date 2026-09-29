import pytest
from shopcart.pricing import apply_percent_discount


def test_discount():
    assert apply_percent_discount(50, 20) == 40.00


def test_bad_percent():
    with pytest.raises(ValueError):
        apply_percent_discount(10, 150)
