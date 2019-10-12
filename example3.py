#test case description
#1. open a browser
#2. go to 24.html file

from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
html_file = os.getcwd()+ "/htmlPages/24_clickable_dropdown.html"
driver.get("file:///"+html_file)

#3. click dropdown button
dropdown = driver.find_element_by_css_selector("body > div > button")
dropdown.click()
time.sleep(1)
#4. click about button
elem = driver.find_element_by_css_selector("#myDropdown > a:nth-child(2)")
elem.click()
time.sleep(1)


