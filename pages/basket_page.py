from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def basket_is_empty(self):
        curr_empy = "Your basket is empty. Continue shopping"
        assert self.if_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Element is not present"
        empty_text_of_basket_page = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
        assert empty_text_of_basket_page == curr_empy

    def basket_is_not_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), "Basket is not empty"