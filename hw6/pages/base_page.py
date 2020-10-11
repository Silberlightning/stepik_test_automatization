from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators
from .locators import MainPageLocators
from selenium.webdriver.support.ui import Select


class BasePage():
    def __init__(self, browser: object, url: object, timeout: object = 10) -> object:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def change_language(self, language):
        select = Select(self.browser.find_element(*BasePageLocators.LANGUAGE))
        select.select_by_value(language)
        button = self.browser.find_element(*BasePageLocators.LANGUAGE_BUTTON)
        button.click()

    def language_is_changed(self, language):
        button_text = self.browser.find_element(*BasePageLocators.LANGUAGE_BUTTON).text
        if language == "ar":
            assert button_text == 'نفّذ', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "ca":
            assert button_text == 'Anar', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "cs":
            assert button_text == 'Provést', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "da":
            assert button_text == 'Udfør', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "de":
            assert button_text == 'Ausführen', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "en-gb":
            assert button_text == 'Go', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "el":
            assert button_text == 'Μετάβαση', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "es":
            assert button_text == 'Ir', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "fi":
            assert button_text == 'Suorita', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "fr":
            assert button_text == 'Envoyer', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "it":
            assert button_text == 'Vai', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "ko":
            assert button_text == '실행', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "nl":
            assert button_text == 'Uitvoeren', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "pl":
            assert button_text == 'Wykonaj', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "pt":
            assert button_text == 'Ir', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "pt-br":
            assert button_text == 'Ir', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "ro":
            assert button_text == 'Start', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "ru":
            assert button_text == 'Выполнить', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "sk":
            assert button_text == 'Vykonať', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "uk":
            assert button_text == 'Вперед', 'Language " ' + str(language) + '" is not correct changed'
        elif language == "zh-hans":
            assert button_text == 'Go', 'Language " ' + str(language) + '" is not correct changed'
        else:
            print("Language is not changed")

    def choose_item(self):
        open_item = self.browser.find_element(*BasePageLocators.ICON_ITEM)
        open_item.click()

    def leave_notification(self, email):
        email_field = self.browser.find_element(*BasePageLocators.EMAIL)
        email_field.send_keys(email)
        notify_button = self.browser.find_element(*BasePageLocators.NOTIFY_BUTTON)
        notify_button.click()

    def is_notification_sent(self):
        try:
            notification = self.browser.find_element(*BasePageLocators.NOTIFY_SENT)
            print("Notification is sent")
        except(NoSuchElementException):
            print("Item is not in stock")
        return True

    # not used anymore
    def add_to_wishlist(self):
        wishlist_button = self.browser.find_element(*BasePageLocators.ADD_WISHLIST)
        wishlist_button.click()

    def is_item_in_stock(self):
        try:
            self.browser.find_element(*BasePageLocators.IN_STOCK)
            print("Item is on stock")
        except(NoSuchElementException):
            print("Item is not in stock")
        return True

    def add_item_to_cart(self):
        add_button = self.browser.find_element(*BasePageLocators.CART_BUTTON)
        add_button.click()

    def should_be_in_cart(self):
        added_item = self.browser.find_element(*BasePageLocators.IN_CART)
        assert added_item.text != 0, "Item added in the cart differs from searched one"

    def search_for_item(self, searched_item):
        search_field = self.browser.find_element(*BasePageLocators.SEARCH_FIELD)
        search_field.send_keys(searched_item)
        search_button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON)
        search_button.click()

    def searched_item_result(self):
        count_searched_item = self.browser.find_element(*BasePageLocators.SEARCH_RESULT)
        search_result = int(count_searched_item.text)
        assert search_result > 0, 'No items found'

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_cart_page(self):
        link = self.browser.find_element(*MainPageLocators.CART_LINK)
        link.click()

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
