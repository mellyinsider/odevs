from selenium.webdriver.common.by import By
from AmazonSEL.Base.Methods import Methods
from AmazonSEL.Page.CategoryPage import categorypage

class wishlistpage(Methods):
    remove_button = (By.ID, "a-autoid-7")

    def remove(self):
        self.selector_exists(categorypage.third_product)
        self.wait_element_clickable(self.remove_button).click()

