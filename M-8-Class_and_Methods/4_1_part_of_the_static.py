class Laptop:
    def __init__(self, brand, age):
        self.brand = brand
        self.age = age

    def increase_age(self, age=100):
        self.last_age = self.age
        self.age = self.age +age

    def repair(self, life_increase = -500):
        self.increase_age(-7000)




my_laptop = Laptop('Lenovo' , 25)
my_laptop.increase_age()
my_laptop.age = 50
my_laptop.increase_age()
my_laptop.increase_age()
my_laptop.increase_age()
print(my_laptop.age)
my_laptop.repair(-9000)
print(my_laptop.age)

print(my_laptop.__dict__)