j=0
k=0
l=0
for i in range(1,11):
    if i==1:
        print(l, end=" ")
        l=1
    elif i==2:
        print(l, end=" ")
        k=l
    else:
        if i == 10 :
            print(l)
            break
        print(l, end= " ")
        j=k
        k=l
        l=j+k


        
    