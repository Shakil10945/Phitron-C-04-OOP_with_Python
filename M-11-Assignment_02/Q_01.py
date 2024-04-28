def exp(x,y):
    multiple =1
    for _ in range(y) :
        multiple *=x
    
    return multiple

x,y = map(int, input("Enter the inputs: ").split())

result = exp(x,y)
print(f"Result is {result}")