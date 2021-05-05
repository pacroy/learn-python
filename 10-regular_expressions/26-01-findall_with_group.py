import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9999'))  # return a list of macthed string

phoneRegex = re.compile(r'(\d\d\d-)\d\d\d-\d\d\d\d')
print(phoneRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9999'))

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9999'))  # return a list of tuples

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9999'))  # return a list of tuples
