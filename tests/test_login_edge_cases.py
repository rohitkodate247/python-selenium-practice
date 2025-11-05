# tests/test_login_edge_cases.py
"""
Covers negative and edge-case login scenarios.
"""

from config import settings


def test_locked_out_user_cannot_login(login_page):
    # Act
    login_page.login(settings.LOCKED_OUT_USER, settings.VALID_PASSWORD)

    # Assert
    error_text = login_page.wait_for_error()
    assert "Sorry, this user has been locked out." in error_text


def test_empty_username_shows_error(login_page):
    # Act
    login_page.login("", settings.VALID_PASSWORD)

    # Assert
    error_text = login_page.wait_for_error()
    assert "Username is required" in error_text


def test_empty_password_shows_error(login_page):
    # Act
    login_page.login(settings.VALID_USERNAME, "")

    # Assert
    error_text = login_page.wait_for_error()
    assert "Password is required" in error_text
