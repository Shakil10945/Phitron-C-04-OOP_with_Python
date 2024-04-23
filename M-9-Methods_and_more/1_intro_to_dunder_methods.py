class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
    def __add__(self, other):
        return self.money + other.money


alim = Person('Alim', 19, 500)
dalim = Person("Dalim", 17, 70)

print(alim+dalim)