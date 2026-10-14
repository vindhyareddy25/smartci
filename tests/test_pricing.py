import pytest
from src.pricing import apply_discount, add_tax


def test_apply_discount():
    assert apply_discount(100, 10) == 90.0


def test_apply_discount_zero():
    assert apply_discount(100, 0) == 100.0


def test_apply_discount_invalid():
    with pytest.raises(ValueError):
        apply_discount(100, 110)


def test_add_tax():
    assert add_tax(100, 0.18) == 118.0