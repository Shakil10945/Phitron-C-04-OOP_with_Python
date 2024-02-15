#Number 1 way.............
"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

exp_dict = dict(zip(keys, values))

print(exp_dict)
"""

#Method 2.........

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

exp_dict = {}
for i in range(len(keys)):
    exp_dict[keys[i]] = values[i]
print(exp_dict)