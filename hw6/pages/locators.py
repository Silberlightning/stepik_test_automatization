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
    LOGIN_MAIL = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[value='Log In']")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SEARCH_FIELD = (By.CSS_SELECTOR, '#id_q')
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[value='Search']")
    SEARCH_RESULT = (By.CSS_SELECTOR, ".form-horizontal strong")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    IN_CART = (By.CSS_SELECTOR, ".alertinner")
    LANGUAGE = (By.CSS_SELECTOR, "#language_selector select")
    LANGUAGE_BUTTON = (By.CSS_SELECTOR, "button")
    ICON_ITEM = (By.CSS_SELECTOR, "img")
    ADD_WISHLIST = (By.CSS_SELECTOR, "a.btn-lg")
    IN_STOCK = (By.CSS_SELECTOR, ".product_main .instock")
    EMAIL = (By.ID, "id_email")
    NOTIFY_BUTTON = (By.CSS_SELECTOR, '.btn-info.btn-lg')
    NOTIFY_SENT = (By.CSS_SELECTOR, '.alertinner')


class ProductPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ITEM_ADDED = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_IN_THE_CART = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE_OF_THE_ITEM = (By.CSS_SELECTOR, ".product_main p.price_color")
    ITEM_TITEL = (By.CSS_SELECTOR, ".product_main h1")
