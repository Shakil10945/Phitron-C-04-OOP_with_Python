def make_upper(st):
    st2=""

    for i in st:
        if 'a'<=i<='z' :
            st2+= chr(ord(i)-ord('a')+ord('A'))
        else:
            st2+=i
    print(st2)
def make_capital(st):
    st2=''
    if('a'<=st[0]<='z'):
        st2+=chr(ord(st[0])-ord('a')+ord('A'))
    else:
        st2+=st[0]
    for i in range(1,len(st)):
        if('A'<=st[i]<='Z'):
            st2+=chr(ord(st[i])-ord('A')+ord('a'))
        else:
            st2+=st[i]
    print(st2)
def make_lower(st):
    st2=""
    for i in st:
        if 'A'<=i<='Z':
            st2+=chr(ord(i)-ord('A')+ord('a'))

        else:
            st2+=i
    print(st2)



s = "HELLppiyjgvnUO SHddkieAKILiiioloo"
make_upper(s)
make_capital(s)
make_lower(s)

