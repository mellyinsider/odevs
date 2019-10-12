#test case description
#1. open a browser
#2. go to python.org
#3. web page title contains word python

#bu implicit wait. shouldnt use.
from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
driver.get("https://www.python.org")
assert 'python' in driver.title.lower()
driver.execute_script("document.body.style.zoom = '1.5'")

time.sleep(2)


# expilicit wait. bu aşağıdakiler kütüphanelerdir.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
###about id'li element sayfada locate oluncaya yani var oluncaya kadar web driverım 10 sn beklesin. 10 sn içinde gelmezse patlasın.
elem = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "about")))

#driver.save_screenshot("screenshot.png")
driver.save_screenshot('screen_shot/ex1.png')
#driver.get_screenshot_as_file('screen_shot/ex_2.png')
driver.close()