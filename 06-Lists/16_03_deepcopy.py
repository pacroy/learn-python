import copy

spam = ['A', 'B', 'C', 'D']
print(spam)
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)
