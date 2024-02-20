def make_upper(st):
    st2=""

    for i in st:
        if 'a'<=i<='z' :
            st2+= chr(ord(i)-ord('a')+ord('A'))
        else:
            st2+=i
    print(st2)

s = "Hello shakil"
make_upper(s)
make_capital()
make_lower()

