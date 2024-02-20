def create_list(dict):
    list=[]
    print(dict)
    for element in dict:
        list.append(element)
        list.append(dict[element])
    print(list)
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
create_list(d)