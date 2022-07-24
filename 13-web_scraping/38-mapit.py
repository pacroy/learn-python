#!/usr/bin/env python
# Open Google Map at given address
# Usage: ./38-mapit.py <place to search>
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print('Address: ' + address)

# webbrowser.open() opens web browser at specified URL
webbrowser.open('https://www.google.co.th/maps/search/' + address)
