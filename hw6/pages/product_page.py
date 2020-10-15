from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser: object, url: object, timeout: object = 10) -> object:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def add_item_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        link.click()

    def check_item_name_in_the_cart(self):
        item_in_the_cart = self.browser.find_element(*ProductPageLocators.SUCCESS_ITEM_ADDED)
        return item_in_the_cart.text

    def check_item_name_on_product_page(self):
        item_product_page = self.browser.find_element(*ProductPageLocators.ITEM_TITEL)
        return item_product_page.text

    def should_be_in_the_cart(self):
        assert self.check_item_name_in_the_cart() == self.check_item_name_on_product_page(), "Item in the cart is not the same as added"

    def check_item_price_in_the_cart(self):
        item_in_the_cart = self.browser.find_element(*ProductPageLocators.PRICE_IN_THE_CART)
        return item_in_the_cart.text

    def check_item_price_on_product_page(self):
        item_product_page = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_ITEM)
        return item_product_page.text

    def should_be_items_price(self):
        assert self.check_item_price_in_the_cart() == self.check_item_price_on_product_page() \
            , "Cart total and item's price differs"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ITEM_ADDED), \
            "Success message is presented, but should not be"

    def is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ITEM_ADDED), \
            "Success message is not disappeared"
