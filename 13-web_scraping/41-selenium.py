#!/usr/bin/env python3
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://automatetheboringstuff.com/")
elements = browser.find_element_by_css_selector("body > div.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a")

print(elements)
