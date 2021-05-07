import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

# sub() method will substitute matched strings
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))

# Use \1 to refer to matched group 1
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))

# Verbose mode
phoneNumberRegex = re.compile(r'''
(\d\d\d-)|      # Area code
(\(\d\d\d\) )   # or Area code wiuth parentheses and no dash
\d\d\d          # First 3 digits
-               # Second dash
\d\d\d\d        # Last 4 digits
\sx\d{2,4}      # Extension like x1234''', re.VERBOSE | re.IGNORECASE | re.DOTALL)  # Pipe (|) is a bitwise operator
