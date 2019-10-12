#test case description
#1. open a browser
#2. go to 25.html file

from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
html_file = os.getcwd()+ "/htmlPages/25_radio_buttons.html"
driver.get("file:///"+html_file)
time.sleep(1)
#1.5 lük zoom yapıcaz
driver.execute_script("document.body.style.zoom = '1.5'")
time.sleep(2)

#inputunun içinde value'su male olanı bul ona tıkla diyoruz.  Çünkü aynı classlar ama 3 farklı value var. female, male, other diye.
elem = driver.find_element_by_css_selector("input[value='male']")
elem.click()

#male clickable olur, diğerleri unclickable olur. find_element ile 1 tane element bulur. 1 tane male olanı bulduk. find_ELEMENTS ile ise
#bütün elementlere bakar. Burada bütün elementleri check edip, clickable olup olmama durumunu yazıyoruz.
buttons = driver.find_elements_by_css_selector('input')
for b in buttons:
    print('button:{} \t checked:{}'.format(b.get_attribute('value'),b.get_attribute('checked')))

