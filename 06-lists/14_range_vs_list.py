spam = list(range(0, 20, 2))
print(spam)
print(spam[1:4])
print('==============================')

def printList(aList):
    for i in range(len(aList)):
        print('Index ' + str(i) + ' in the list is ' + supplies[i])

supplies = ['pens', 'staples', 'puncher', 'binders']
printList(supplies)
animals = ['cat', 'dog', 'rat', 'elephant']
printList(animals)