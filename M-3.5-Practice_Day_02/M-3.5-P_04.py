word = input()
num=0
cap=0
low=0
sym=0

for i in word:
    if ord(i)>=48 and ord(i)<=57:
        num+=1
    elif ord(i)>=65 and ord(i)<=90:
        cap+=1
    elif ord(i)>=97 and ord(i)<=122:
        low+=1
    else:
        sym+=1
        
print(f'Capital = {cap}')
print(f'Lower = {low}')
print(f'Number = {num}')
print(f'Symbol = {sym}')
        