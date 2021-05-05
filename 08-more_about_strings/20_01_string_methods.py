# String methods usually give you a new string as string is immutable
spam = 'Hello world!'
print('01: ' + spam.upper())
print('02: ' + spam)
spam = spam.upper()
print('03: ' + spam)
print('04: ' + spam.lower())
print('05: ' + spam)

print('==============================')

# Check input string
answer = 'YeS'
if answer.lower() == 'yes':
    print('Playing again')

print('==============================')

# islower() and isupper()
spam = 'Hello world!'
print('islower: ' + str(spam.islower()))
spam = 'HELLO WORLD!'
print('isupper: ' + str(spam.isupper()))
print('Hello'.upper())
print('Hello'.upper().isupper())

print('==============================')

# Other methods
## isalpha()    = letters only
## isalnum()    = letters and numbers only
## isdecimal()  = numbers only
## isspace()    = whitespaces only
## istitle()    = Titlecase only

print("'hello'.isalpha()           = " + str('hello'.isalpha()))
print("'hello123'.isalpha()        = " + str('hello123'.isalpha()))
print("'hello123'.isalnum()        = " + str('hello123'.isalnum()))
print("'123'.isdecimal()           = " + str('123'.isdecimal()))
print("'   '.isspace()             = " + str('   '.isspace()))
print("'Hello world!'[5].isspace() = " + str('Hello world!'[5].isspace()))
print("'This Is Title.'.istitle()  = " + str('This Is Title Case.'.istitle()))
print("'hello world!'.title()      = " + str('hello world!'.title()))

print('==============================')

# startswith() and endswith()
print('Hello world!'.startswith('Hello'))
print('Hello world!'.startswith('H'))
print('Hello world!'.startswith('ello'))
print('Hello world!'.endswith('world!'))
print('Hello world!'.endswith('world'))

print('==============================')

# join()
print("join()")
print(','.join(['cats', 'rats', 'bats']))
print(''.join(['cats', 'rats', 'bats']))
print('\n\n'.join(['cats', 'rats', 'bats']))

print('==============================')

# split()
print("join()")
print('My name is Simon'.split())
print('My name is Simon'.split('m'))

print('==============================')

# ljust() and rjust() and center()
print("ljust() and rjust() and center()")
print("'" + 'Hello'.rjust(10) + "'")
print("'" + 'Hello'.ljust(10) + "'")
print("'" + 'Hello'.rjust(20, '*') + "'")
print("'" + 'Hello'.ljust(25, "-") + "'")

print("'" + 'Hello'.center(20) + "'")
print("'" + 'Hello'.center(20, '=') + "'")

print('==============================')

# strip() and lstrip() and rstrip()
print("strip() and lstrip() and rstrip()")
spam = 'Hello'.rjust(10)
print("'" + spam + "'")
print("'" + spam.strip() + "'")
print("'" + '     x     '.strip() + "'")
print("'" + '     x     '.lstrip() + "'")
print("'" + '     x     '.rstrip() + "'")
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))

print('==============================')

# replace()
print("replace()")
spam = 'Hello there!'
print(spam.replace('e', 'XYZ'))
