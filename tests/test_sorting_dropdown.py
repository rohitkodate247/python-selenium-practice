# tests/test_sorting_dropdown.py
"""
Demonstrates interacting with a dropdown (sorting).
You can extend this to actually verify order by price/name.
"""

from config import settings
from pages.inventory_page import InventoryPage


def test_user_can_change_sorting_option(login_page, driver):
    login_page.login(settings.VALID_USERNAME, settings.VALID_PASSWORD)
    inventory_page = InventoryPage(driver)

    # Action: change sort to "Price (low to high)"
    inventory_page.select_sort_option("Price (low to high)")

    # For now, just assert page is still showing products
    # (in advanced version, you'd get item prices and check ordering)
    count = inventory_page.get_product_count()
    assert count > 0, "Products should still be visible after sorting"
