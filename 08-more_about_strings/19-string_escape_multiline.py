# String literal using single quote or double quote
string1 = "This is Alice's cats"

# Use escape character
## \' = Single quote
## \" = Double quote
## \t = Tab
## \n = Newline (line break)
## \\ = Backslash
string2 = 'This is Alice\'s cats'
print('Hello there!\nHow are you?\nI\'m fine.')

# Raw string will be processed without being escaped
print(r'That is Carol\'s cat.')

print('==============================')

# Multiline string using """ or ```
print("""Dear Alice,
Eve's cat has been arrested for catnapping, cat buglary, and extortion.
Sincerely,
Bob""")
print('==============================')
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat buglary, and extortion.
Sincerely,
Bob''')

print('==============================')

spam = 'Hello world!'
print(spam[0])
print(spam[1:5])
print(spam[-1])
print('Hello' in spam)
print('HELLO' in spam)
