class Vehicle:
    District = "Shariatpur"
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass

School_bus = Bus("Ena", 180, 2800)
School_bus.District = "Pabna"
print(School_bus.__dict__)

School_bus.capacity = 680
print(School_bus.__dict__)

print(type(School_bus))

print(isinstance(School_bus, Vehicle))
