# dot (.) means character except the newline
import re

# Set re.DOTALL to include newline for dot (.)
dotStarRegex = re.compile(r'.*')
print(dotStarRegex.findall('Serve the public trust.\nProtect the innocent.\nUpload the law.'))
dotStarRegex = re.compile(r'.*', re.DOTALL)
print(dotStarRegex.findall('Serve the public trust.\nProtect the innocent.\nUpload the law.'))

# Set re.IGNORECASE to ignore case, making case-insensitive
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Alex, howdy?'))
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowelRegex.findall('Alex, howdy?'))
vowelRegex = re.compile(r'[aeiou]', re.I)   # re.I is shorthand of re.IGNORECASE
print(vowelRegex.findall('Alex, howdy?'))
