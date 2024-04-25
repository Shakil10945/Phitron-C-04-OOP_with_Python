class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

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
print("Name:", school_bus.name)
print("Mileage:", school_bus.mileage)
print("Capacity:", school_bus.capacity)
print()

print("Sedan:")
print("Name:", sedan.name)
print("Mileage:", sedan.mileage)
print("Capacity:", sedan.capacity)
print()

print("Truck:")
print("Name:", truck.name)
print("Mileage:", truck.mileage)
print("Capacity:", truck.capacity)
print()

print("Pickup:")
print("Name:", pickup.name)
print("Mileage:", pickup.mileage)
print("Capacity:", pickup.capacity)
