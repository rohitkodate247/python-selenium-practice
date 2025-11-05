# pages/inventory_page.py
"""
Page Object for the Inventory page (after successful login).
This helps us write cleaner tests for product listing, add-to-cart, sorting, etc.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        self.driver = driver

    def get_product_count(self) -> int:
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        return len(items)

    def add_first_item_to_cart(self):
        """
        Clicks the first visible 'Add to cart' button.
        In a real test, you might parameterize which item to add.
        """
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if buttons:
            buttons[0].click()

    def get_cart_count(self) -> int:
        """Return the number shown in the cart badge. 0 if not present."""
        badges = self.driver.find_elements(*self.SHOPPING_CART_BADGE)
        if not badges:
            return 0
        return int(badges[0].text)

    def select_sort_option(self, visible_text: str):
        """Select a sort option from the dropdown by visible text."""
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(visible_text)
