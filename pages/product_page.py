import time
from .base_page import BasePage, solve_quiz_and_get_code
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_the_basket(self):
        WebDriverWait(self.browser, 12).until(
            EC.presence_of_element_located(ProductPageLocators.ADD_TO_BASKET)).click()
        solve_quiz_and_get_code(self)
        time.sleep(5)

    def should_book_name_equals_hints_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        print(book_name.text)
        assert book_name.text == self.browser.find_element(*ProductPageLocators.ADDED_BOOK).text

    def should_book_price_equals_hints_name(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        print(book_price.text)
        assert book_price.text == self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
