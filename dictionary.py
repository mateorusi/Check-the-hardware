counts = dict()
names = ['mateo', 'ledion', 'done', 'ledion', 'mateo']
for name in names :
    counts[name] = counts.get(name , 0) + 1
print(counts)
