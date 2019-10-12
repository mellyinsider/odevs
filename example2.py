#test case description
#1. open a browser
#2. go to 23.html file

from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
html_file = os.getcwd()+"/htmlPages/23.html"
driver.get("file:///"+html_file)

#3. check "I have a bike" checkbox.
time.sleep(3)
elem = driver.find_element_by_css_selector("body > form:nth-child(1) > input[type=checkbox]:nth-child(1)")
elem.click()
time.sleep(2)
elem.click()
print(elem.get_attribute('checked'))
time.sleep(2)
#4. check button enabled or not
button = driver.find_element_by_css_selector('#disabled_button')
button.click()
print(button.is_enabled())
time.sleep(2)
#5. Click "click me" button
button = driver.find_element_by_css_selector('body > button:nth-child(4)')
print(button.is_enabled())
time.sleep(2)
# send keys
text_field = driver.find_element_by_css_selector("body > form:nth-child(11) > input[type=text]:nth-child(8)")
text_field.send_keys("blahblah")
time.sleep(2)
#clear text field
text_field.clear()
time.sleep(2)

