from collections import defaultdict
d=defaultdict(list)
people = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 30},
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
]
for i in people:
    if i['age'] in d:
        d[i['age']].append(i['name'])
    else:
        d[i['age']].append(i['name'])
d=dict(d)
print(d)