"""Entry point: python -m shopcart.cli"""
from shopcart.cart import Cart


def main():
    cart = Cart()
    cart.add_item("pen", 1.50, 4)
    cart.add_item("notebook", 3.25, 2)
    cart.add_item("pen", 1.50, 2)  # should make 6 pens
    cart.apply_coupon("SAVE10")
    print(f"Subtotal: {cart.subtotal():.2f}")
    print(f"Total:    {cart.total():.2f}")


if __name__ == "__main__":
    main()
