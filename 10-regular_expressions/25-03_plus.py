# + matches one or more times
import re

batRegex = re.compile(r'Bat(wo)+man')

matchObject = batRegex.search('The Adventures of Batman')
try:
    print(matchObject.group())
except AttributeError:
    print('Cannot find any bat(wo)+man')
matchObject = batRegex.search('The Adventures of Batwoman')
print(matchObject.group())
matchObject = batRegex.search('The Adventures of Batwowowoman')
print(matchObject.group())
