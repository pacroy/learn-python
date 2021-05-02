# String in Python is immutable (cannot be changes)
# This may no longer valid!!!
name = 'Zophie'
name_list = list(name)
name_list[5] = 'X'
print(name)
print(name_list)
print('==============================')

# Use slice to get new string
name = 'Zophie a cat'
newName = name [0:7] + 'the' + name [8:12]
print(newName)
print('==============================')
