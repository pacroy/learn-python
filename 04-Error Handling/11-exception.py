print('How many cats do you own?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('This is a lot of cats.')
    else:
      print('That is not that many cats.')    
except ValueError:
    print('You did not enter a number.')