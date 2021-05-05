# {n} matches exactly n times
import re

batRegex = re.compile(r'(Ha){3}')
matchObject = batRegex.search('He said HaHaHa')
print(matchObject.group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
matchObject = phoneRegex.search('My numbers are 415-555-1234,415-666-5678,212-555-0000')
print(matchObject.group())
