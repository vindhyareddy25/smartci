import pytest
from src.inventory import Inventory


def test_add_stock():
    inventory = Inventory()
    inventory.add_stock("Pen", 10)
    inventory.add_stock("Pen", 5)
    assert inventory.stock["Pen"] == 15


def test_remove_stock():
    inventory = Inventory()
    inventory.add_stock("Book", 10)
    inventory.remove_stock("Book", 3)
    assert inventory.stock["Book"] == 7


def test_remove_more_than_available():
    inventory = Inventory()
    inventory.add_stock("Book", 2)

    with pytest.raises(ValueError):
        inventory.remove_stock("Book", 5)