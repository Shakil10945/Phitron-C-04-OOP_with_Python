def create_new_string(a, s):
    s = s.split(' ')
    for i in s:
        if i.endswith(','):
            x = s.index(i)
            stm = ''
            for j in range(len(s[x]) - 1):
                stm += s[x][j]
            s[x] = stm
        elif i.endswith('.'):
            x = s.index(i)
            stm = ''
            for j in range(len(s[x]) - 1):
                stm += s[x][j]
            s[x] = stm

    st2 = ''
    for i in range(len(s) - 1):
        if s[i].lower() in [word.lower() for word in a]:
            st2 += s[i + 1] + " "

    with open('out.txt', 'w') as file:
        file.write(st2)

a = ['oh', 'Emelia', 'to']
s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

create_new_string(a, s)
