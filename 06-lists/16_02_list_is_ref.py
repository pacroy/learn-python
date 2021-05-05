# List is a reference variable
spam = list(range(0,6))
print(spam)
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
print(spam)
print('==============================')

def eggs(someParameter):
    someParameter.append('Hello')

spam = list(range(1,4))
print(spam)
eggs(spam)
print(spam)
