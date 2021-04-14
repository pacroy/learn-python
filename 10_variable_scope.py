spam = 42   # global variable
eggs = 64   # global variable

def func():
    global eggs
    spam = 24   # local variable
    print('Local spam is ' + str(spam))
    print('Global eggs is ' + str(eggs))
    eggs = 86   # global variable

print('Global spam is ' + str(spam))
func()
print('Global spam is ' + str(spam))
print('Global eggs is ' + str(eggs))