num=input()
x=len(num)
b=1
for i , j in zip(range(0,x) , range(x-1,0,-1)):
    if num[i] != num[j]:
        b=0

if b==0:
    print("False")
else:
    print("True")