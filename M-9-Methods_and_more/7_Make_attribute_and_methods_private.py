class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password
    
    def __get_pass(self):
        print(self.__password)
    
    def user_log(self,name, passd):
        if(self.name == name, self.__password == passd):
            return True
        return False



ryan = User("shakil", "ASDF")
#print(ryan.name)
#print(ryan.__password)
#ryan.__get_pass()
print(ryan.user_log('shakil', "ASDF"))