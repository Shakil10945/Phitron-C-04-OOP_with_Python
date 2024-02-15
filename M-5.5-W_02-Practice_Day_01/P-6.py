sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
# Keys to extract
keys = ["name", "salary"]

exp_dict = {}
for i in range(len(keys)):
    exp_dict[keys[i]] = sample_dict[keys[i]]

print(exp_dict)


