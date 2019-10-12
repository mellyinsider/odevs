#test case description
#1. open a browser
#2. go to page.html file

from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
html_file = os.getcwd()+ "/htmlPages/page.html"
driver.get("file:///"+html_file)
time.sleep(2)

#dikkat!!! büyük-küçük harf duyarlı...

try:
    assert 'Your file was not found' not in driver.page_source
except AssertionError:
    print('Error: page not found, check URL')

driver.close()