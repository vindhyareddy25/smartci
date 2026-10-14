from src.cart import Cart


def test_add_item():
    cart = Cart()
    cart.add("Pen", 10, 2)
    assert cart.total() == 23.6


def test_cart_with_discount():
    cart = Cart()
    cart.add("Book", 100, 1)
    assert cart.total(discount=10) == 106.2