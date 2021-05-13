import shelve

# shelve will creates 3 files to store our values
shelfFile = shelve.open('mydata')
# shelfFile is like a dictionary
shelfFile['cats'] = ['Zophie', 'Pook', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
print(shelfFile.keys())
shelfFile.close()
