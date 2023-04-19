from selenium.common import NoSuchElementException


from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # def is_element_present(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except (NoSuchElementException):
    #         return False
    #     return True

    def should_verify_empty_basket_message(self):
        header = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
        print(header.text)
        assert header.text == 'Your basket is empty. Continue shopping'

    def should_verify_empty_basket_content(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), 'Basket not empty'

