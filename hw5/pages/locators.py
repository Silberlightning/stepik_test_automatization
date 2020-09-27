from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.CSS_SELECTOR, "a[href*=basket]")
    CART_ITEM_INSIDE = (By.CSS_SELECTOR, ".thumbnail")
    CART_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ITEM_ADDED = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_IN_THE_CART = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE_OF_THE_ITEM = (By.CSS_SELECTOR, ".product_main p.price_color")
    ITEM_TITEL = (By.CSS_SELECTOR, ".product_main h1")



