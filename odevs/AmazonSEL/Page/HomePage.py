from AmazonSEL.Base.Methods import Methods
from selenium.webdriver.common.by import By


class homepage (Methods):
    login_icon = (By.ID, "nav-link-accountList")
    search_bar = (By.ID, "twotabsearchtextbox")
    search_icon = (By.CLASS_NAME, "nav-input")

    def enter_login_icon(self):
        self.wait_element_clickable(self.login_icon).click()

    def search_text(self, text):
        self.wait_element_clickable(self.search_bar).click()
        self.wait_element_clickable(self.search_bar).send_keys(text)
        self.wait_element_clickable(self.search_icon).click()






