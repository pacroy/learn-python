# {x ,y} matches at least x times, at most y times
import re

batRegex = re.compile(r'(Ha){3,5}')
matchObject = batRegex.search('He said HaHaHa')
print(matchObject.group())


matchObject = batRegex.search('He said HaHaHaHaHa')
print(matchObject.group())

batRegex = re.compile(r'(Ha){3,}')
matchObject = batRegex.search('He said HaHaHaHaHa')
print(matchObject.group())

print('==============================')

digitRegex = re.compile(r'(\d){3,5}')
matchObject = digitRegex.search('1234567890')
print(matchObject.group())  # Match longest string possible aka. greedy match (default)

print('==============================')

digitRegex = re.compile(r'(\d){3,5}?')
matchObject = digitRegex.search('1234567890')
print(matchObject.group())  # Match shortest string posible aka. non-greedy match
