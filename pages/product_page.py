'''описать метод добавления в корзину'''
import time

from selenium.webdriver.common.by import By
from .base_page import BasePage, solve_quiz_and_get_code
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_the_basket(self):
        WebDriverWait(self.browser, 12).until(
            EC.presence_of_element_located(ProductPageLocators.ADD_TO_BASKET)).click()
        solve_quiz_and_get_code(self)
        time.sleep(10)

    def should_book_name_equals_hints_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        print(book_name.text)
        assert book_name.text == self.browser.find_element(*ProductPageLocators.ADDED_BOOK).text

    def should_book_price_equals_hints_name(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        print(book_price.text)
        assert book_price.text == self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text
