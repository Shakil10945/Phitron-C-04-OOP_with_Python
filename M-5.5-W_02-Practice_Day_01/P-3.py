def mechanic(l1,l2):
    lx=[]
    for i in range(0,len(l1)):
        lx.append(l1[i]+l2[i])
    
    return lx
        

l1=["M", "na", "i", "Bo"]
l2=["y", "me", "s", "nd"]

lx=mechanic(l1,l2)
print(lx)