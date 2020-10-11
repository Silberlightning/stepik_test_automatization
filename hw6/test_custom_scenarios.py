import pytest
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import time


@pytest.mark.need_review_custom_scenarios
def test_user_can_sign_in(browser):
    email = 'example2@gmail.com'
    password = 'testimpo20'
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.user_sign_in(email, password)
    page.should_be_authorized_user()


@pytest.mark.need_review_custom_scenarios
def test_guest_can_find_item_by_name(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    searched_item = 'Design'
    page = BasePage(browser, link)
    page.open()
    page.search_for_item(searched_item)
    page.searched_item_result()


@pytest.mark.need_review_custom_scenarios
def test_guest_can_add_item_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    searched_item = 'Design'
    page = BasePage(browser, link)
    page.open()
    page.search_for_item(searched_item)
    page.searched_item_result()
    page.add_item_to_cart()
    page.should_be_in_cart()


@pytest.mark.need_review_custom_scenarios
def test_guest_can_change_site_languange(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    language = 'en-gb'
    page = BasePage(browser, link)
    page.open()
    page.change_language(language)
    page.language_is_changed(language)


@pytest.mark.need_review_custom_scenarios
def test_whether_item_on_stock(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    searched_item = 'Design'
    page = BasePage(browser, link)
    page.open()
    page.search_for_item(searched_item)
    page.searched_item_result()
    page.choose_item()
    page.is_item_in_stock()


@pytest.mark.need_review_custom_scenarios
def test_guest_can_leave_notification_for_items_not_on_stock(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    searched_item = 'Hacking Exposed'
    email = str(time.time()) + "@fakemail.org"
    page = BasePage(browser, link)
    page.open()
    page.search_for_item(searched_item)
    page.searched_item_result()
    page.choose_item()
    page.leave_notification(email)
    page.is_notification_sent()
