word=input()

word2=""

for i in range(0,len(word)):
    if ord(word[i])>=65 and ord(word[i])<=90 :
        word2+= chr(ord(word[i]) +32)
    elif ord(word[i])>=97 and ord(word[i])<=122 :
        word2+= chr(ord(word[i]) -32)
    else:
        word2 +=word[i]
print(word2)