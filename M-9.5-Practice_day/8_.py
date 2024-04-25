class Vehicle:
    def __init__(self, name, mileage, capacity):
        self._name = name
        self._mileage = mileage
        self._capacity = capacity

    def get_name(self):
        return self._name

    def get_mileage(self):
        return self._mileage

    def get_capacity(self):
        return self._capacity

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

class Sedan(Car):
    pass

class Truck(Vehicle):
    pass

class Pickup(Vehicle):
    pass

# Creating instances
school_bus = Bus("School Volvo", 12, 50)
sedan = Sedan("Toyota Camry", 25, 5)
truck = Truck("Ford F150", 18, 3)
pickup = Pickup("Chevrolet Silverado", 15, 2)

# Outputs
print("School Bus:")
print("Name:", school_bus.get_name())
print("Mileage:", school_bus.get_mileage())
print("Capacity:", school_bus.get_capacity())
print()

print("Sedan:")
print("Name:", sedan.get_name())
print("Mileage:", sedan.get_mileage())
print("Capacity:", sedan.get_capacity())
print()

print("Truck:")
print("Name:", truck.get_name())
print("Mileage:", truck.get_mileage())
print("Capacity:", truck.get_capacity())
print()

print("Pickup:")
print("Name:", pickup.get_name())
print("Mileage:", pickup.get_mileage())
print("Capacity:", pickup.get_capacity())
