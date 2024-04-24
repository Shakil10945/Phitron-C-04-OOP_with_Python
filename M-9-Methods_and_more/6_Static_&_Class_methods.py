class Shopping:
    mall = "jamuna future park"
    hours = 10
    def __init__(self, customer):
        self.customer = customer
        self.item = []
        self.total = 0
    
    @classmethod
    def opening_hour(cls, day):
        return cls.mall

    @staticmethod
    def multiply(x,y):
        return x*y
        
    def add_to_cart(self, item, price, qunatity):
        itme_total = price*qunatity
        self.total += item_total
        self.item.append(item)

result = Shopping.multiply(5,6)
print(result)

my_shoping = Shopping('alll')

res = Shopping.multiply(5,69)
print(res)

clss3 = Shopping.opening_hour(7)
print(clss3)