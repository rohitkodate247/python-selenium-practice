"""
Driver factory: create and configure WebDriver instances.
This keeps driver setup out of the tests.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import settings
import os


def get_driver():
    chrome_options = Options()

    # run headless in CI environments
    if os.getenv("CI", "false").lower() == "true":
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(settings.IMPLICIT_WAIT)
    return driver
