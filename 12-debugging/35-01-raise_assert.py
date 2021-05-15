# raise creates a new exception for any user's error
try:
    raise  Exception('This is the error message.')
except Exception:
    print('Exception was raised.')

import traceback

print('====================')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be equal or greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

boxPrint('*', 5, 5)
boxPrint('O', 10, 5)

print('====================')

# traceback.format_exc() prints error trace
try:
    boxPrint('**', 5, 5)
except Exception:
    print('Exception was raised.')
    print(traceback.format_exc())

try:
    boxPrint('*', 1, 1)
except Exception:
    print('Exception was raised.')
    print(traceback.format_exc())

print('====================')

# assert is programmer's error to do sanity check to ensure a condition should never be false
try:
    assert False, 'This is error message.'
except AssertionError:
    print(traceback.format_exc())
    