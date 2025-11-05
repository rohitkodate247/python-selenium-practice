import pytest
from config import settings


@pytest.mark.parametrize(
    "username,password,expected_text",
    [
        # locked out user
        (settings.LOCKED_OUT_USER, settings.VALID_PASSWORD,
         "Sorry, this user has been locked out."),
        # empty username
        ("", settings.VALID_PASSWORD, "Username is required"),
        # empty password
        (settings.VALID_USERNAME, "", "Password is required"),
        # wrong password
        (settings.VALID_USERNAME, settings.INVALID_PASSWORD, "Epic sadface"),
    ],
)
def test_login_negative_parametrized(login_page, username, password, expected_text):
    """
    Single test that covers multiple login failure scenarios.
    This shows you know how to reduce duplication and improve maintainability.
    """
    login_page.login(username, password)
    error_text = login_page.wait_for_error()
    assert expected_text in error_text
