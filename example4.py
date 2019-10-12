#test case description
#1. open a browser
#2. go to 24.html file

from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
html_file = os.getcwd()+ "/htmlPages/24_hoverable_dropdown.html"
driver.get("file:///"+html_file)

#3. hover to "mouse over me"
elem = driver.find_element_by_css_selector("body > div > span")
ActionChains(driver).move_to_element(elem).perform()
time.sleep(2)

#4. click the hello world
elem = driver.find_element_by_css_selector("body > div > div > p")
print(elem.text)

driver.quit()
