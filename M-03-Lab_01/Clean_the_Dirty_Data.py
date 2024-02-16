data = "aNtEriOur\n\t>>"

data = data.lower()

new_data=""
new_data2=""

for i,j in zip(data,range(len(data))):
    if (i=="a") or (i=='e') or (i=="i") or (i=="o") or (i=="u"):
        if(j==len(data)-1):
            new_data+=i
        else:   
            new_data+=i+"_"
for i in range(len(new_data)-1):
    new_data2+=new_data[i]
print(new_data2)