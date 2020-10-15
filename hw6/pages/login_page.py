from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser: object, url: object, timeout: object = 10) -> object:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def register_new_user(self, email, password):
        self.should_be_register_form()
        mail = self.browser.find_element(*LoginPageLocators.REGISTER_MAIL)
        mail.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        button.click()

    def user_sign_in(self, email, password):
        self.should_be_login_form()
        mail = self.browser.find_element(*LoginPageLocators.LOGIN_MAIL)
        mail.send_keys(email)
        password_login = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password_login.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found"
        assert True

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"
        assert True
