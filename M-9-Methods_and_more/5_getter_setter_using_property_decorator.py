class User:
    def __init__(self, f_name, l_name):
        self.first = f_name
        self.last = l_name
        self.email = f"{self.first}.{self.last}@gmail.com"

    @property
    def full_name(self):
        return f"{self.first}{self.last}"
    
    def get_email(self):
       return self.email
        

mark = User('mark', 'zuku')
print(mark.first)
print(mark.last)
print(mark.get_email())
print(mark.full_name)