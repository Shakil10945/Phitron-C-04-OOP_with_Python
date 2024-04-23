def first_fun():
    print("here's the first one")
    def secon_fun():
        print("Second one started")
    
    return secon_fun

first_fun()()

# dak = first_fun()
# dak()

# print(dak)