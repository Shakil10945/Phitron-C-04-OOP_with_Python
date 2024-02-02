l1=[10, 20, 30, 40]
l2=[100, 200, 300, 400]
 
lx= list(zip(l1, reversed(l2)))

for i in range(0,len(lx)):
    print(lx[i][0],"\t" ,lx[i][1])
    #print(f'{lx[i][0]} \t {lx[i][1]}')