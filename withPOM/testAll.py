import unittest
from selenium import webdriver
from page import HomePage
from page import AboutPage
from locator import CommonPageLocators
from locator import AboutPageLocators

class TestPyOrgBase(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.close()

class TestHome(TestPyOrgBase):
    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)

    def test_TC001_py3_doc_button(self):
        self.home.hover_to(CommonPageLocators.DOC)
        self.home.assert_elem_text(CommonPageLocators.PY3_DOC_BUTTON, 'Python 3.x Docs')
        self.home.click(CommonPageLocators.PY3_DOC_BUTTON)
        assert self.driver.current_url == 'https://docs.python.org/3/'

    def test_TC002_blahblah_search(self):
        self.home.search_for('blahblah')
        self.home.assert_elem_text(CommonPageLocators.SEARCH_RESULT_LIST, 'No results found.')


class TestAbout(TestPyOrgBase):
    def setUp(self):
        super().setUp()
        self.about = AboutPage(self.driver)

    def test_TC003_upcoming_events_check(self):
        self.about.assert_elem_text(AboutPageLocators.UPCOMING_EVENTS, 'Upcoming Events')

if __name__ == '__main__':
    unittest.main()