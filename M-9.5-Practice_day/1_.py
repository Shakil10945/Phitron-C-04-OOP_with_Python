class School:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.email = f"{self.name}.{self.roll}@gmail.com"
    

rid = School("hridoy", 19)
print(rid.__dict__)
