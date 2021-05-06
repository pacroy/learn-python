# dot (.) means character except the newline
import re

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# .* means anything
nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
print(nameRegex.findall('First name: Chairat Last name: Onyaem'))

# .* is greedy match by default
greedyRegex = re.compile(r'<(.*)>')
print(greedyRegex.findall('<To serve humans> for dinner.>'))

# Append ? for non-greedy match
nongreedyRegex = re.compile(r'<(.*?)>')
print(nongreedyRegex.findall('<To serve humans> for dinner.>'))
