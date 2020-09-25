from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)    #initiate PageObject, give driver and url to constructor
    page.open()
    page.go_to_login_page()
