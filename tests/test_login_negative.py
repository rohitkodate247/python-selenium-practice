"""
Negative login test.
Shows you can validate error states, not just happy path.
"""

from config import settings


def test_login_with_invalid_password(login_page):
    # Act
    login_page.login(settings.VALID_USERNAME, settings.INVALID_PASSWORD)

    # Assert
    error_text = login_page.wait_for_error()
    assert "Epic sadface" in error_text, "Error message should be shown for invalid credentials"
