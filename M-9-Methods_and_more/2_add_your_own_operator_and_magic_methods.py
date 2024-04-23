class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
    def __add__(self, other):
        return self.money + other.money
    
    def __call__(self):
        print(f"This is {self.name} with age {self.age} and he has {self.money}")

    def __eq__(self, other):
        return self.age == other.age


alim = Person('Alim', 19, 500)
dalim = Person("Dalim", 17, 70)


alim()

print(alim+dalim)
print(alim == dalim)