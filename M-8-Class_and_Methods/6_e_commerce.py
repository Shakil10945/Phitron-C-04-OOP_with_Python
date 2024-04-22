class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        self.cart.append({'item' : item, 'price' : price, 'quantity' : quantity})

    def checkout(self, amount):
        price = 0
        for item  in self.cart:
            price += item['price'] * item['quantity']

        if amount< price:
            return f'please give me more money: {price -amount}'
        elif amount> price:
            return f'Here is your extra money: {amount -price}'
        else:
            return 'here is are the items'
        

shopping = Shopper("Big Bazaaaar")
shopping.add_to_cart("Shirt", 500, 5)
shopping.add_to_cart("Pant", 600, 4)
shopping.add_to_cart("Panjabi", 700, 6)

reply = shopping.checkout(7000)
print(reply)