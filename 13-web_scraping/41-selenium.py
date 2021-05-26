#!/usr/bin/env python3
# pip install selenium
# Install WebDriver from https://www.selenium.dev/downloads/
#   - Egde driver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads
# Add installation folder to Path environment variable
from selenium import webdriver

driver = webdriver.Edge(executable_path="msedgedriver.exe")
driver.get("https://automatetheboringstuff.com/")
driver.implicitly_wait(5)

element = driver.find_element_by_css_selector("body > div.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a")
element.click()
driver.implicitly_wait(3)

print('====================')

elements = driver.find_elements_by_css_selector("#calibre_link-1171 > p.copy2")
print(elements[0].text.strip())

print('====================')

driver.get("https://www.w3schools.com/html/html_forms.asp")
driver.implicitly_wait(3)

element = driver.find_element_by_css_selector("#fname")
element.send_keys('Zophie')
element.submit()

print('====================')

driver.quit()
