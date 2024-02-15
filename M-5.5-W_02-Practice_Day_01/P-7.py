sample_dict = {'a': 100, 'b': 200, 'c': 300}

for i in range(len(sample_dict)):
    if(list(sample_dict.values())[i] == 100):
        print("Present")
        break
else:
    print("Not Present") 