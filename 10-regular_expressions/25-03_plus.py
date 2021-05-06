# + matches one or more times
import re

batRegex = re.compile(r'Bat(wo)+man')

matchObject = batRegex.search('The Adventures of Batman')
print(matchObject == None)
matchObject = batRegex.search('The Adventures of Batwoman')
print(matchObject.group())
matchObject = batRegex.search('The Adventures of Batwowowoman')
print(matchObject.group())
