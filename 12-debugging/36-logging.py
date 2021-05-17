# Log level sequence
# logging.CRITICAL
# logging.ERROR
# logging.WARNING
# logging.INFO
# logging.DEBUG
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# To log to a file, add filename='file' to basicConfig():
# logging.basicConfig(filename='program.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    
    logging.debug('Return value is %s' % (total))
    return total

print (factorial(5))

logging.debug('End of program')

print('====================')

logging.disable(logging.CRITICAL)   # Turn off all logging
logging.debug('Start of program')

def factorial2(n):
    logging.debug('Start of factorial2(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    
    logging.debug('Return value is %s' % (total))
    return total

print (factorial2(5))

logging.debug('End of program')

