import re

# regex groups are specified with ( parentheseses )
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('My phone number is 415-555-4242')

print(matchObject.group(1))
print(matchObject.group(2))

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search('My phone number is (415) 555-4242')

print(matchObject.group())

print('==============================')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
matchObject = batRegex.search('Batmobile lost a wheel')
print(matchObject.group())

matchObject = batRegex.search('Batmotorcycle lost a wheel')
try:
    print(matchObject.group())
except AttributeError:
    print('Cannot find any bat*')
