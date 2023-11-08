from selenium import webdriver
import json

from page import LoginPage

with open('config.json') as f:
    CONFIG = json.load(f)


def run():
    driver = webdriver.Chrome()
    driver.get(CONFIG["address_login_page"])

    # Load the main page. In this case the home page
    login_page = LoginPage(driver)
    login_page.is_title_matches()
    login_page.fill_form("standard_user", "secret_sauce")
    login_page.click_login_button()

    driver.quit()


if __name__ == "__main__":
    run()
