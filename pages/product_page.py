from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.if_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Dont find button Add To Basket"
        link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        link.click()


    def compararsion_of_elements(self):
        assert self.if_element_present(*ProductPageLocators.ITEM_ADDED_TO_BASKET), "Dont find information about item in basket"
        assert self.if_element_present(*ProductPageLocators.NAME_OF_BOOK), "Dont find name of book"
        assert self.if_element_present(*ProductPageLocators.PRICE_OF_BOOK), "Dont find price of book"
        assert self.if_element_present(*ProductPageLocators.PRICE_IN_BASKET), "Dont find price in basket"
        item_added_to_basket = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TO_BASKET).text
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        assert item_added_to_basket == name_of_book, "Text is not equal"
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price_of_book == price_in_basket, "Price is not equal"