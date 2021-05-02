# Dictionaries are key-value pairs
myCat = {'size': 'fat', \
         'color': 'gray', \
         'disposition': 'loud'}
print('My cat has ' + myCat['color'] + 'fur.')

# Key can be numbers
spam = {12345: 'Luggage combination', \
        42: 'The Answer'}
print('==============================')

# Key-value pairs in dictionaries are unordered
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
hams = {'species': 'cat', 'name': 'Zophie', 'age': 8}
print(eggs == hams)     # True
print('==============================')

# Unlike lists, they are ordered
print([1, 2, 3] == [3, 2, 1])

# Getting undefined key returns KeyError exception
try:
    print(eggs['color'])        # KeyError
except KeyError:
    print('Undefined key')
