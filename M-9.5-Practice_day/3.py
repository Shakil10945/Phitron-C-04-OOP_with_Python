class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def __str__(self):
        return f"Vehicle: {self.name}, Mileage: {self.mileage}, Capacity: {self.capacity}"



class Bus(Vehicle):
    pass


School_bus = Bus("Ena", 150, 300)

print(School_bus)

print(str(School_bus))