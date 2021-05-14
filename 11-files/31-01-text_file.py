import os

# open() opens file in read-only mode
helloFile = open('hello.txt')
# read() reads file as a single string
print(helloFile.read())
# close() closes the openned file
helloFile.close()

helloFile = open('hello.txt')
# readlines() returns as a list of string each line
print(helloFile.readlines())
helloFile.close()

# with 'a', it opens file in append mode, file will be created if not exists
# with 'w', it opens file in write mode
helloFile = open('hello2.txt', 'w')
helloFile.write('I\'m fine, thank you\n')
helloFile.write('Where did you go last night?\n')
helloFile.write('Did you enjoy the night?\n')
helloFile.close()

# Clean up
os.remove('hello2.txt')
