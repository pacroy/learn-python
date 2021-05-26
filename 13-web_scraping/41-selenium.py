#!/usr/bin/env python3
# pip install selenium
# Install WebDriver from https://www.selenium.dev/downloads/
#   - Egde driver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads
# Add installation folder to Path environment variable
# Go to https://selenium-python.readthedocs.io/ for more information
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
def document_initialised(driver):
    return driver.execute_script("return initialised")

driver = webdriver.Edge(executable_path="msedgedriver.exe")
driver.get("https://automatetheboringstuff.com/")
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element_by_css_selector("body > div.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a"))

element = driver.find_element_by_css_selector("body > div.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a")
element.click()
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element_by_css_selector("#calibre_link-1171 > p.copy2"))

print('====================')

elements = driver.find_elements_by_css_selector("#calibre_link-1171 > p.copy2")
print(elements[0].text.strip())

print('====================')

driver.get("https://www.w3schools.com/html/html_forms.asp")
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element_by_css_selector("#fname"))

element = driver.find_element_by_css_selector("#fname")
element.send_keys('Zophie')
element.submit()


print('====================')

print("Press ENTER to quit...", end='')
input()
print("Quiting...")
driver.quit()
print("Go to https://selenium-python.readthedocs.io/ for more information")
