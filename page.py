from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Object Page for the login page"""

    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        """Verifies that the hardcoded text "Swag Labs" appears in page title
        :return: True if element is in title of page
        """
        return "Swag Labs" in self.driver.title

    def fill_form(self, username: str, password: str):
        """
        Locate and fill the fields of password and username
        :param username: username provided
        :param password: password provided
        :return:
        """
        # Find form elements by their locators (e.g., ID or NAME)
        user_input = self.driver.find_element(*LoginPageLocators.USER_FIELD_LOCATOR)
        pswd_input = self.driver.find_element(*LoginPageLocators.PSWD_FIELD_LOCATOR)

        # Fill out the form fields
        user_input.send_keys(username)
        pswd_input.send_keys(password)

    def click_login_button(self):
        """Find and click the login button after field was filled"""

        button_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON_LOCATOR))
        button_element.click()

    def is_error_message(self):
        """Checks if the error message due to wrong login appears
        :return: True if message is displayed
        """
        wait = WebDriverWait(self.driver, 10)
        message_element = wait.until(EC.presence_of_element_located(LoginPageLocators.ERROR_MESSAGE_LOCATOR))
        return message_element.is_displayed()


class LoginPageLocators:
    """A class for login page locators"""
    LOGIN_BUTTON_LOCATOR = (By.ID, 'login-button')
    USER_FIELD_LOCATOR = (By.ID, 'user-name')
    PSWD_FIELD_LOCATOR = (By.ID, 'password')
    ERROR_MESSAGE_LOCATOR = (By.TAG_NAME, "h3")


class InventoryPage:
    """Object Page for the Inventory Page"""
    def __init__(self, driver):
        self.driver = driver

    def is_page_load_success(self):
        """
        Checks if the page was successfully loaded after login
        :return: True if element is displayed
        """
        wait = WebDriverWait(self.driver, 10)
        title_element = wait.until(EC.presence_of_element_located(InventoryPageLocators.PAGE_TITLE_LOCATOR))
        return title_element.is_displayed()


class InventoryPageLocators:
    """A class for Inventory page locators"""
    PAGE_TITLE_LOCATOR = (By.CLASS_NAME, "title")