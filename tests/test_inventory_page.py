# tests/test_inventory_page.py
"""
Tests related to the inventory page after login.
Shows: navigation, POM usage, and UI validation.
"""

from config import settings
from pages.inventory_page import InventoryPage


def test_inventory_shows_expected_number_of_products(login_page, driver):
    # login first
    login_page.login(settings.VALID_USERNAME, settings.VALID_PASSWORD)

    inventory_page = InventoryPage(driver)
    count = inventory_page.get_product_count()

    assert count == settings.EXPECTED_PRODUCT_COUNT, (
        f"Expected {settings.EXPECTED_PRODUCT_COUNT} products, but found {count}"
    )
