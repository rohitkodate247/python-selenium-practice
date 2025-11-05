"""
Positive login test.
Demonstrates: fixture usage, page object usage, and assertion.
This is close to what Carta may ask you to do in 45 minutes.
"""

from config import settings


def test_login_with_valid_credentials(login_page, driver):
    # Act
    login_page.login(settings.VALID_USERNAME, settings.VALID_PASSWORD)

    # Assert
    # On success, saucedemo redirects to /inventory.html
    assert "inventory.html" in driver.current_url, "User should land on inventory page after valid login"
