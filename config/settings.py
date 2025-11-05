"""
Central place to store test settings.
In a real project, you might read from env vars or a .env file.
"""

BASE_URL = "https://www.saucedemo.com/"  # good demo site
BROWSER = "chrome"  # could be 'firefox' if you add geckodriver
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_PASSWORD = "wrong_password"
IMPLICIT_WAIT = 10
