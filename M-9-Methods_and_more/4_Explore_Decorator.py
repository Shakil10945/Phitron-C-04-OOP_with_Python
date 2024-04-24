import math
def timer(func):
    def inner(*arg):
        print("Time Starts now")
        func(*arg)
        print("Time just ended")

    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f"Factorial of {n} is: {result}")

get_factorial(8)
#timer(get_factorial)()