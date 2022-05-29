import time
import unittest
from selenium import webdriver
import page
import time


class AutomationPractice(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://dev-company.profesi.io")
        time.sleep(2)

    def test_create_assessment(self):
        mainPage = page.MainPage(self.driver)
        self.driver.implicitly_wait(30)
        mainPage.login_apps()
        mainPage.login_button()
        time.sleep(3)
        mainPage.create_assessment()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()