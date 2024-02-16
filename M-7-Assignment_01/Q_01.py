def create_string(list):
    str = ""
    for i in list:
        if i==len(list)-1 :
            str+=i
        else:
            str += i + " "
    print(str)

l = ["This", "is", "very", "fantastic"]

create_string(l)
