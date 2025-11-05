# tests/test_add_to_cart.py
"""
Validates that after login, user can add an item to the cart.
This mimics a real user workflow and is good interview material.
"""

from config import settings
from pages.inventory_page import InventoryPage


def test_user_can_add_item_to_cart(login_page, driver):
    # login
    login_page.login(settings.VALID_USERNAME, settings.VALID_PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_first_item_to_cart()

    cart_count = inventory_page.get_cart_count()
    assert cart_count == 1, "Cart count should be 1 after adding one item"
