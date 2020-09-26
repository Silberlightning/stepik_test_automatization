from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ITEM_ADDED = (By.CSS_SELECTOR, ".alertinner")
    PRICE_IN_THE_CART = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE_OF_THE_ITEM = (By.CSS_SELECTOR, ".price_color")
    ITEM_TITEL = (By.CSS_SELECTOR, ".product_main h1")

