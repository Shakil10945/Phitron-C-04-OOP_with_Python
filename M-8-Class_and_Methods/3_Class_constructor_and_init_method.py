class Phone:
    manufactured = "India"

    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price 
        self.color = color

    def sms(self, text, number):
        print(f'Sms: {text}, sending to: {number}')


my_phone = Phone('Samsung', 30000, 'red')

her_phone = Phone('Iphone', 150000, 'white')

print(my_phone.brand,my_phone.color,my_phone.price,my_phone.manufactured)
print(her_phone.color, her_phone.price, her_phone.brand)