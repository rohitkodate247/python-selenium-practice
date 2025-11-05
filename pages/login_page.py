"""
Page Object for the login page on saucedemo.com
This shows you understand POM, which senior QA roles care about.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def load(self, base_url: str):
        """Navigate to the login page."""
        self.driver.get(base_url)

    def login(self, username: str, password: str):
        """Perform login with provided credentials."""
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def wait_for_error(self, timeout=5):
        """Wait for error message to appear and return its text."""
        wait = WebDriverWait(self.driver, timeout)
        elem = wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return elem.text
