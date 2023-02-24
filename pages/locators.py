from selenium.webdriver.common.by import By
# from .base_page import BasePage

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group:nth-child(2) > a")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "login_link")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    NAME_OF_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner")

class BasketPageLocators():
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_IS_NOT_EMPTY = (By.CSS_SELECTOR, ".col-sm-6.h3")

