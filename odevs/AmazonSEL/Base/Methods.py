from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class Methods(object):

    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        return WebDriverWait(self.driver, 30)

    def wait_element_clickable(self, element):
        return self.wait().until(ec.element_to_be_clickable(element))

    def wait_element_visible(self, element):
        return self.wait().until(ec.visibility_of_element_located(element))

    def hover(self, element):
        hover_element = self.wait_element_clickable(element)
        hvr = ActionChains(self.driver).move_to_element(hover_element)
        hvr.perform()

    def selector_exists(self, element):
        try:
            return self.wait_element_clickable(element)
        except TimeoutException:
            return False



