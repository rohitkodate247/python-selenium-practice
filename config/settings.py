"""
Central place to store test settings.
In a real project, you might read from env vars or a .env file.
"""

BASE_URL = "https://www.saucedemo.com/"  # good demo site
BROWSER = "chrome"  # could be 'firefox' if you add geckodriver

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


# Additional users from SauceDemo’s test data
LOCKED_OUT_USER = "locked_out_user"

INVALID_PASSWORD = "wrong_password"
IMPLICIT_WAIT = 10

# for inventory validation
EXPECTED_PRODUCT_COUNT = 6  # saucedemo shows 6 products by default
