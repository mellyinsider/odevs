from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.meetup.com/TestHive/')
driver.get('https://www.stackoverflow.com/')
element = driver.find_element_by_name('q')
element.send_keys('selenium webdriver')
element.send_keys(Keys.ENTER)