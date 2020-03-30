from selenium.webdriver.common.by import By
from AmazonSEL.Base.Methods import Methods

class loginpage(Methods):
    email_textbox = (By.ID, "ap_email")
    continue_button = (By.ID, "continue")
    password_textbox = (By.ID, "ap_password")
    login_button = (By.ID, "signInSubmit")

    def login(self, email, password):
        self.wait_element_clickable(self.email_textbox).send_keys(email)
        self.wait_element_clickable(self.continue_button).click()
        self.wait_element_clickable(self.password_textbox).send_keys(password)
        self.wait_element_clickable(self.login_button).click()




