#!/usr/bin/env python
# pip install requests
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# raise_for_status() will raise an exception if there's any error
res.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
