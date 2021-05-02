cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size, color, disposition)

size, color, disposition = 'skinny', 'black', 'quiet'
print(size, color, disposition)

a = 'AAA'
b = 'BBB'
a, b = b, a
print(a, b)

spam = 42
spam += 1
print(spam)