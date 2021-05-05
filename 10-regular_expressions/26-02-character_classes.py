# Character classes
# \d = Any numeric digit from 0 to 9
# \D = Any character that is NOT a numeric digit from 0 to 9
# \w = Any letter, numeric digit, or the underscore character = word.
# \W = Any character that is NOT a letter, numeric digit, or the underscore character
# \s = Any space, tab, or newline character = whitespace
# \S = Any character that is NOT a space, tab, or newline character

import re

digitRegex = re.compile(r'(\d)')
digitRegex2 = re.compile(r'(0|1|2|3|4|5|6|7|8|9)')

print(digitRegex.findall('This is 12345, 6789'))
print(digitRegex2.findall('This is 12345, 6789'))

print('==============================')

lyrics = '12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming, 6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves, and 1 Partridge in a Pear Tree'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

print('==============================')

# Use [...] for subset of characters
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food.'))

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food.'))

print('==============================')

# [^...] caret (^) negates subset of characters
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food.'))
