cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'}
allCats = []
allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'})
allCats.append({'name': 'Pooka', 'age': 5, 'color': 'black'})
allCats.append({'name': 'Fat-tail', 'age': 3, 'color': 'gray'})
allCats.append({'name': '???', 'age': -1, 'color': 'orange'})

# Data structure represents a Tic-Tac-Toe Board
#  | |  
# -----
#  | |  
# -----
#  | |  
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', \
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', \
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

# type()
print(type(42))
print(type(3.14))
print(type(theBoard))
