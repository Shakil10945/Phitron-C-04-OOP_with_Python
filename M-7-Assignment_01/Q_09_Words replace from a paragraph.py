def replaced_version(lst, st):
    st=st.split(' ')
    for i in st:
        for j in lst:
            if i==j:
                x=st.index(i)
                y=lst.index(j)
                st[x]=lst[y+1]
    st = ' '.join(st)
    print(type(st))
    print(st)
                
replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
replaced_version(replace_with,s)

