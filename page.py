from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Class for the login page  """

    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        """Verifies that the hardcoded text "Swag Labs" appears in page title"""
        return "Swag Labs" in self.driver.title

    def fill_form(self, username: str, password: str):
        # Find form elements by their locators (e.g., ID or NAME)
        user_input = self.driver.find_element(*LoginPageLocators.USER_FIELD_LOCATOR)
        pswd_input = self.driver.find_element(*LoginPageLocators.PSWD_FIELD_LOCATOR)

        # Fill out the form fields
        user_input.send_keys(username)
        pswd_input.send_keys(password)

    def click_login_button(self):
        """Triggers the search"""

        button_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON_LOCATOR))
        button_element.click()


class LoginPageLocators:
    """A class for main page locators. All main page locators should come here"""

    LOGIN_BUTTON_LOCATOR = (By.ID, 'login-button')
    USER_FIELD_LOCATOR = (By.ID, 'user-name')
    PSWD_FIELD_LOCATOR = (By.ID, 'password')


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def is_page_load_success(self):
        wait = WebDriverWait(self.driver, 10)
        title_element = wait.until(EC.presence_of_element_located(InventoryPageLocators.PAGE_TITLE_LOCATOR))

        return title_element.is_displayed()


class InventoryPageLocators:

    PAGE_TITLE_LOCATOR = (By.CLASS_NAME, "title")