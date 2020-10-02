import pytest
import time
from selenium.webdriver.common.by import By


def test_guest_can_register(browser):
    #Go to login page
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

    #Fill out register form
    email = str(time.time()) + "@fakemail.org"
    password = "Zuccini15%%"
    mail = browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
    mail.send_keys(email)
    password1 = browser.find_element(By.CSS_SELECTOR,"#id_registration-password1")
    password1.send_keys(password)
    password2 = browser.find_element(By.CSS_SELECTOR,"#id_registration-password2")
    password2.send_keys(password)

    #Click register button
    button = browser.find_element(By.CSS_SELECTOR,"#register_form .btn")
    button.click()

    #Assertion: text is right
    assert browser.find_element(By.CSS_SELECTOR, ".wicon").text == "Thanks for registering!",\
        "No message about successful registration :("

