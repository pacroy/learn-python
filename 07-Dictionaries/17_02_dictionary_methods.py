# keys(), values(), items()
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))
print('==============================')

for k in eggs.keys():
    print(k)
print('==============================')

for k in eggs.values():
    print(k)
print('==============================')

for k, v in eggs.items():
    print(k, v)
for i in eggs.items():      # as tuple
    print(i)
print('==============================')

# Check key before access
## using ifs
if 'color' in eggs:
    print('color=' + eggs['color'])
if 'age' in eggs:
    print('age=' + str(eggs['age']))

## using get()
print('color=' + str(eggs.get('color', 0)))
print('age=' + str(eggs.get('age', 0)))

print('==============================')

# setDefault()
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
if 'color' not in eggs:
    eggs['color'] = 'black'
print(eggs)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
eggs.setdefault('color', 'black')
print(eggs)
eggs.setdefault('color', 'orange')
print(eggs)
