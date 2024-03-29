from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'Login' is not in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username input is missing"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password input is missing"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register email input is missing"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register password input is missing"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_REPEAT), "Register repeat password input " \
                                                                                     "is missing"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button input is missing"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
