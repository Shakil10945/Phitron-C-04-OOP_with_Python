class Vehicle:
    District = "Shariatpur"
    def __init__(self, name, mileage, capacity):
        self.name = name
        self._mileage = mileage
        self.__capacity = capacity
    @property
    def get_info(self):
        print(self.name)
        print(self._mileage)
        print(self.__capacity)


class Bus(Vehicle):
    pass

School_bus = Bus("Ena", 180, 2800)
School_bus.District = "Pabna"
# print(School_bus.__dict__)

# School_bus.capacity = 680
# print(School_bus.__dict__)

# print(type(School_bus))

# print(isinstance(School_bus, Vehicle))

School_bus.get_info
