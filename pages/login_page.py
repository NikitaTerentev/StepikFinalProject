from .base_page import BasePage
from .locators import LoginPageLocators
import faker

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.if_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found ! "

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.if_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form not found !"

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        password = "12345asdf"
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMT).click()



