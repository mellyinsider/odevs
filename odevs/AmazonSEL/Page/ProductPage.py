from AmazonSEL.Base.Methods import Methods
from selenium.webdriver.common.by import By


class productpage(Methods):
    wishlist_button = (By.ID, "wishListMainButton")
    show_list_button = (By.CLASS_NAME, "w-button-inner")

    def addWishList(self):
        self.wait_element_clickable(self.wishlist_button).click()
        self.wait_element_clickable(self.show_list_button).click()
