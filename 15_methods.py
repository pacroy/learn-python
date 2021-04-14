spam = ['hello', 'hi', 'howdy', 'heyas', 'howdy']
print(spam.index('howdy'))
try:
    print(spam.index('test'))
except ValueError:
    print('test not found')
print('==============================')

spam.append('moose')
print(spam)
spam.insert(1, 'chicken')
print(spam)
spam.remove('howdy')
print(spam)
del spam[4]
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
print('==============================')

spam = ['Alice', 'badgers', 'ants', 'Bob', 'cats']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)