from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        link.click()

    def should_be_in_the_cart(self):
        item_text_in_the_cart = self.browser.find_element(*ProductPageLocators.SUCCESS_ITEM_ADDED)
        item_text_main = self.browser.find_element(*ProductPageLocators.ITEM_TITEL)
        assert item_text_in_the_cart.text == item_text_main.text, "Item in the cart is not the same as added"

    def should_be_items_price(self):
        price_in_the_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_THE_CART)
        price_of_the_item = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_ITEM)
        assert price_in_the_cart.text == price_of_the_item.text, "Cart total and item's price differs"

