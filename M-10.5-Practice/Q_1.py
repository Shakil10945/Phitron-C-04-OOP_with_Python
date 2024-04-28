class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def ne_name(self, new_name, new_id, new_salary):
        self.name = new_name
        self.id = new_id
        self.salary =new_salary
    
    def __repr__(self) -> str:
        return(f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}")
    
emp_1 = Employee("Shakil", "EBDF68", 70000)

print(type(Employee))
print(type(emp_1))
print(emp_1)

print(emp_1.__dict__)
print(emp_1.__module__)

emp_1.ne_name("Romjan", "XXXXXXXXXXXX", 40)

print(emp_1)
print(emp_1.__dict__)