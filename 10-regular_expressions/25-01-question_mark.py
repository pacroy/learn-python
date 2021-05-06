# ? matches zero or one time
import re

batRegex = re.compile(r'Bat(wo)?man')
matchObject = batRegex.search('The Adventures of Batman')
print(matchObject.group())

matchObject = batRegex.search('The Adventures of Batwoman')
print(matchObject.group())

matchObject = batRegex.search('The Adventures of Batwowowoman')
print(matchObject == None)

print('==============================')

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneRegex.search('My phone number is 415-555-4242')
print(matchObject.group())

matchObject = phoneRegex.search('My phone number is 555-4242')
print(matchObject == None)

print('==============================')

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
matchObject = phoneRegex.search('My phone number is 415-555-4242')
print(matchObject.group())

matchObject = phoneRegex.search('My phone number is 555-4242')
print(matchObject.group())
