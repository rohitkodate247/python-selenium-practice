"""
Pytest fixtures shared across tests.
This is where we create and tear down the driver.
"""

import pytest
from utils.driver_factory import get_driver
from config import settings
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    """
    Returns a LoginPage that is already opened.
    This makes tests very clean.
    """
    page = LoginPage(driver)
    page.load(settings.BASE_URL)
    return page
