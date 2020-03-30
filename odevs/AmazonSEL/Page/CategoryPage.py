from selenium.webdriver.common.by import By
from AmazonSEL.Base.Methods import Methods


class categorypage(Methods):
    assert_samsung = (By.CSS_SELECTOR, "#search > span > div > span > h1 > div > div.sg-col-14-of-20.sg-col-26-of-32.sg-col-18-of-24.sg-col.sg-col-22-of-28.s-breadcrumb.sg-col-10-of-16.sg-col-30-of-36.sg-col-6-of-12 > div > div > span.a-color-state.a-text-bold")
    second_page_button = (By.CSS_SELECTOR, "#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(10) > div > div > span > div > div > ul > li:nth-child(3)")
    third_product = (By.XPATH , '//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div')
    #third_product = (By.CSS_SELECTOR, "#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(5) > div:nth-child(1) > div:nth-child(3) > div > span > div > div > div:nth-child(2) > div.sg-col-4-of-12.sg-col-8-of-16.sg-col-16-of-24.sg-col-12-of-20.sg-col-24-of-32.sg-col.sg-col-28-of-36.sg-col-20-of-28 > div > div:nth-child(1) > div > div > div:nth-child(1) > h2 > a > span")

    def click_second_page(self):
        assert_samsung = self.wait_element_visible(categorypage.assert_samsung).text
        assert (assert_samsung == '"samsung"')
        self.wait_element_clickable(self.second_page_button).click()
        self.wait_element_clickable(self.third_product).click()

