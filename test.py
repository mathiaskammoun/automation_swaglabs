from selenium import webdriver
import unittest

import json

from page import LoginPage, InventoryPage

with open('config.json') as f:
    CONFIG = json.load(f)


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(CONFIG["address_login_page"])

    def test_successful_login(self):
        """
        Test lusha.com contact sales feature
        :return:
        """

        # Load the main page. In this case the home page
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.is_title_matches(), "Login Page successfully loaded")

        # Test for successful login
        login_page.fill_form("standard_user", "secret_sauce")
        login_page.click_login_button()
        inventory_page = InventoryPage(self.driver)
        self.assertTrue(inventory_page.is_page_load_success(), "Login was not successful")

    def test_wrong_login(self):
        # Load the main page. In this case the home page
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.is_title_matches(), "Login Page successfully loaded")

        # Test for wrong password login
        login_page.fill_form("standard_user", "secret_auce")
        login_page.click_login_button()
        self.assertTrue(login_page.is_error_message(), "Error message did not appear after login attempt")

        # Test for wrong username login
        login_page.fill_form("stauser", "secret_sauce")
        login_page.click_login_button()
        self.assertTrue(login_page.is_error_message(), "Error message did not appear after login attempt")

        # Test for both wrong username and login
        login_page.fill_form("abc", "123")
        login_page.click_login_button()
        self.assertTrue(login_page.is_error_message(), "Error message did not appear after login attempt")

    def tearDown(self):
        self.driver.quit()




