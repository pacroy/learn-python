# US phone number matcher without regex
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
                return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
                return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
                return False
    return True

print(isPhoneNumber('415-555-1234'))
print(isPhoneNumber('123,456.78'))

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')