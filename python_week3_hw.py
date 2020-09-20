import random

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# 1.Registration
def user_registration():
    website = "http://selenium1py.pythonanywhere.com/ru/"
    user_login = 'example'
    user_domen = '@gmail.com'
    user_password = 'testimpo20'

    try:

        # Arrange
        browser = webdriver.Chrome()
        browser.get(website)

        number = str(random.randint(1, 1000000))
        user_mail = user_login + number + user_domen

        # Act
        button = browser.find_element_by_id('login_link')
        button.click()

        login = browser.find_element_by_id('id_registration-email')
        login.send_keys(user_mail)

        password1 = browser.find_element_by_id('id_registration-password1')
        password1.send_keys(user_password)

        password2 = browser.find_element_by_id('id_registration-password2')
        password2.send_keys(user_password)

        register = browser.find_element_by_css_selector("[value='Register']")
        register.click()

        # Assertion
        success = browser.find_element_by_id('messages')
        assert "Спасибо за регистрацию" in success.text

    finally:

        browser.quit()

user_registration()

# 2.Sign_in
def user_sign_in():

    website = "http://selenium1py.pythonanywhere.com/ru/"
    user_mail = 'example2@gmail.com'
    user_password = 'testimpo20'

    try:

        # Arrange
        browser = webdriver.Chrome()
        browser.get(website)

        # Act
        button = browser.find_element_by_id('login_link')
        button.click()

        login = browser.find_element_by_id('id_login-username')
        login.send_keys(user_mail)

        password = browser.find_element_by_id('id_login-password')
        password.send_keys(user_password)

        register = browser.find_element_by_css_selector("[value='Log In']")
        register.click()

        # Assertion
        success = browser.find_element_by_id('messages')
        assert "Рады" in success.text

    finally:

        browser.quit()

user_sign_in()

# 3.Add_to_cart
def add_to_cart():
    website = "http://selenium1py.pythonanywhere.com/ru/"
    item = 'Design'

    try:

        # Arrange
        browser = webdriver.Chrome()
        browser.get(website)

        # Act
        input = browser.find_element_by_css_selector('#id_q')
        input.send_keys(item)

        search = browser.find_element_by_css_selector("[value='Найти']")
        search.click()

        add_cart = browser.find_element_by_xpath('//button[text()="Добавить в корзину"]')
        add_cart.click()

        # Assertion
        success = browser.find_element_by_id('messages')
        assert "был добавлен" in success.text

    finally:

        browser.quit()

add_to_cart()

# 4.Translate website

def translate_website():
    website = "http://selenium1py.pythonanywhere.com/ru/"

    try:

        # Arrange
        browser = webdriver.Chrome()
        browser.get(website)

        select = Select(browser.find_element_by_name("language"))
        select.select_by_value('de')

        button = browser.find_element_by_xpath('//button[text()="Выполнить"]')
        button.click()


        # Assertion
        success = browser.find_element_by_xpath('//button')
        assert "Ausführen" in success.text

    finally:

        browser.quit()

translate_website()

print("If not failed, then passed")