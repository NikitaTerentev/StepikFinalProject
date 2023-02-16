from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

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



