import random
from selenium import webdriver
import locators_2

def test_user_registration():

    user_login = 'example'
    user_domen = '@gmail.com'
    user_password = 'testimpo20'

    # Arrange
    browser = webdriver.Chrome()
    browser.get(locators_2.website)

    number = str(random.randint(1, 1000000))
    user_mail = user_login + number + user_domen

    # Act
    button = browser.find_element_by_id(locators_2.button_login)
    button.click()

    login = browser.find_element_by_id(locators_2.mail)
    login.send_keys(user_mail)

    password1 = browser.find_element_by_id(locators_2.password1)
    password1.send_keys(user_password)

    password2 = browser.find_element_by_id(locators_2.password2)
    password2.send_keys(user_password)

    register = browser.find_element_by_css_selector(locators_2.button_register)
    register.click()

    # Assertion
    success = browser.find_element_by_id('messages')
    assert "Спасибо за регистрацию" in success.text

    browser.guit()

