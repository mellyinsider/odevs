import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestPythonOrg(unittest.TestCase):


    def setUp(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('headless')
        chrome_option.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_option)

    def test_TC001_py3_doc_button(self):
        self.driver.get("https://www.python.org")
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID, "documentation")))
        ActionChains(self.driver).move_to_element(element).perform()
        locator ="#documentation > ul > li.tier-2.super-navigation > p.download-buttons > a:nth-child(1)"
        py3button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        assert py3button.text == 'Python 3.x Docs'
        py3button.click()
        assert self.driver.current_url == 'https://docs.python.org/3/'

    def test_TC002(self):
        self.driver.get("https://www.python.org")
        searchBar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#id-search-field")))
        searchBar.send_keys("blah blah")
        go_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#submit")))
        go_button.click()
        assert self.driver.current_url == 'https://www.python.org/search/?q=blah+blah&submit='


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
