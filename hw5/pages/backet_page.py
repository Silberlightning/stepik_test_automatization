from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*MainPageLocators.CART_ITEM_INSIDE), \
            "Some items are in the cart, but should not be"

    def should_be_text_about_empty_cart(self):
        assert self.is_element_present(*MainPageLocators.CART_EMPTY_TEXT), \
            "Text on the page says, the cart isn't empty, but be"
