class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

shopper_1 = Shop("shakil")
shopper_2 = Shop("rayhna")
shopper_1.add_to_cart('shoe')
print(shopper_1.cart)
shopper_2.add_to_cart('pant')
print(shopper_2.cart)
print(shopper_1.cart)