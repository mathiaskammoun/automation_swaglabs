from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Class for the login page  """

    LOGIN_BUTTON_LOCATOR = (By.ID, 'login-button')
    USER_FIELD_LOCATOR = (By.ID, 'user-name')
    PSWD_FIELD_LOCATOR = (By.ID, 'password')

    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Swag Labs" in self.driver.title

    def fill_form(self, username: str, password: str):
        # Find form elements by their locators (e.g., ID or NAME)
        user_input = self.driver.find_element(*self.USER_FIELD_LOCATOR)
        pswd_input = self.driver.find_element(*self.PSWD_FIELD_LOCATOR)

        # Fill out the form fields
        user_input.send_keys(username)
        pswd_input.send_keys(password)


    def click_login_button(self):
        """Triggers the search"""

        button_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_BUTTON_LOCATOR))
        button_element.click()

