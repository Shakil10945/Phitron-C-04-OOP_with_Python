def tx(number_1, number_2, number_3):
    x = []
    
    
    for i in range(1,4):
        l= int(locals()["number_"+str(i)])
        #=int("number_" + str(i))
        #d = int(locals()[l])
        if l<0:
            x.append(-l)
        else:
            x.append(l)
        

    # if a<0:
    #     x.append(-a)
    # else:
    #     x.append(a)
    # if b<0:
    #     x.append(-b)
    # else:
    #     x.append(b)
    # if c<0:
    #     x.append(-c)
    # else:
    #     x.append(c)
    return x

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))

c = tx(a,b,c)
print(c)