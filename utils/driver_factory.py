"""
Driver factory: create and configure WebDriver instances.
This keeps driver setup out of the tests.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import settings


def get_driver():
    """
    Returns a configured Selenium WebDriver instance.
    For interview practice, Chrome is fine.
    In a real framework, this could read BROWSER from env and branch.
    """
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")  # uncomment for headless runs
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(settings.IMPLICIT_WAIT)
    return driver
