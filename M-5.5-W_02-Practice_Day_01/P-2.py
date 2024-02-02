def sum_or_diminish(a,b):
    x=a+b
    y=a-b

    return(x,y)






a = int(input())
b = int(input())

sum,dim = sum_or_diminish(a,b)
print(f"Sum of {a} and {b} is {sum} and Reduction of {a} and {b} is {dim}")
