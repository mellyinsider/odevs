#Test case description
#1. open a browser
#2. go to python.org
#3. web page title contains word python  (lower case yaptı title'ı alarak.)

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.python.org/')
assert 'python' in driver.title.lower()

driver.quit()

#close sessionu, quit driver'ı kapatır.

