import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.backet_page import BasketPage
from .pages.base_page import BasePage
import time


class TestGuestAddPromoItems():
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_item_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_in_the_cart()
        product_page.should_be_items_price()


@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "Zuccini15%%"
        page = BasePage(browser)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_item_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_in_the_cart()
        product_page.should_be_items_price()


class TestGuestFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        basket_page = product_page.go_to_cart_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_cart()
        basket_page.should_be_text_about_empty_cart()
