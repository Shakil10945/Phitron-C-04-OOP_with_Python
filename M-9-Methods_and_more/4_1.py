import math
def timer(func):
    def inner(*args, **kargs):
        print("Time Starts")
        func(*args, **kargs)
        print("Time Ends")
    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'factorial of {n} is: {result}')

get_factorial(35)