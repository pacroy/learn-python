import pprint

message = 'It was a bright colde day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
print('==============================')
ptext = pprint.pformat(count)
print(ptext)
