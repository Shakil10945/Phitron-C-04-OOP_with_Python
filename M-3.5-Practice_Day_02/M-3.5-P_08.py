k=0
l=1

s=int(input())
r=int(input())

for i in range(1,r):
    for j in range(2,i) :
        if i%j==0:
            k=0
            break
        elif(j==i-1 and k==0):
            k=1
            l=i
            break
    if k==1 and  l>=s and l<=r:
        print(l, end=' ')