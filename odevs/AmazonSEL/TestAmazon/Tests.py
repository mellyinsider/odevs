import unittest
from selenium import webdriver
from AmazonSEL.Page.CategoryPage import categorypage
from AmazonSEL.Page.HomePage import homepage
from AmazonSEL.Page.LoginPage import loginpage
from AmazonSEL.Page.ProductPage import productpage
from AmazonSEL.Page.WishListPage import wishlistpage



class amazontest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/melis.al/Downloads/chromedriver")
        self.driver.get('https://www.amazon.com.tr/')

    def testAmazon(self):
        homepage(self.driver).enter_login_icon()
        loginpage(self.driver).login("tezt1zs@gmail.com", "123gm123gm")
        homepage(self.driver).search_text("samsung")
        categorypage(self.driver).click_second_page()
        productpage(self.driver).addWishList()
        wishlistpage(self.driver).remove()

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()