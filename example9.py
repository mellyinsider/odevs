#test case description
#1. open a browser
#2. go to 33.html file

from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
html_file = os.getcwd()+ "/htmlPages/33.html"
driver.get("file:///"+html_file)
time.sleep(2)

driver.find_element_by_css_selector('button').click()
time.sleep(1)
#çıkan pop-upı kabul etmek için
driver.switch_to_alert().accept()
time.sleep(1)

driver.close()
