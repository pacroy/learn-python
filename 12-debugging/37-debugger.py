# Basic debugging exercise
print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)

print('====================')

# Step into/Step over exercise
def function1():
    print('function1')
    function2()

def function2():
    print('function2')

function1()

print('====================')

# Breakpoint exercise
import random

heads = 0
for i in range(1, 1000):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')

print('Heads came up ' + str(heads) + ' times.')
