import pytest
from .pages.product_page import ProductPage

@pytest.mark.xfail(strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)  # initiate PageObject, give driver and url to constructor
    product_page.open()
    product_page.add_item_to_cart()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)  # initiate PageObject, give driver and url to constructor
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail(strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)  # initiate PageObject, give driver and url to constructor
    product_page.open()
    product_page.add_item_to_cart()
    product_page.is_disappeared_success_message()
