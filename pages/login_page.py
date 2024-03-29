from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        assert True, 'There is no Login link'

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        header = self.browser.find_element(*LoginPageLocators.LOGIN_FORM).text
        print(header)
        assert header == 'Войти', 'The Login form is unavailable'

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        header = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM).text
        print(header)
        assert header == 'Зарегистрироваться', 'The Registration form is unavailable'

    def register_new_user(self, email, password):
        self.browser.find_element(By.ID, 'id_registration-email').send_keys(email)
        self.browser.find_element(By.ID, 'id_registration-password1').send_keys(password)
        self.browser.find_element(By.ID, 'id_registration-password2').send_keys(password)
        self.browser.find_element(By.NAME, 'registration_submit').click()
