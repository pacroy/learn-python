#!/usr/bin/env python3
# pip install beautifulsoup4
import bs4, requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
res = requests.get("https://www.bloomberg.com/energy", headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

# In Edge/Chrome, open Developer tools -> Select an element,  right-click on the tag and select Copy -> selector
elements = soup.select('#content > div > div > div.section-front__main-content > div.data-tables.first > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > span')

print('WTI Crude Oil Price: ' + elements[0].text.strip() + ' USD/bbl.')
