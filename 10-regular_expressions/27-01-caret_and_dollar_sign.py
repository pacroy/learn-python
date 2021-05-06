import re

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.findall('Hello there!'))
print(beginsWithHelloRegex.findall('He said "Hello!"'))

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.findall('Hello world!'))
print(endsWithWorldRegex.findall('Hello worldometer!'))

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.findall('164501363523553431'))
print(allDigitsRegex.findall('164501363x23553431'))
