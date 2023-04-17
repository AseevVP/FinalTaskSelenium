from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form > h2')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form > h2')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    BOOK_NAME = (By.TAG_NAME, 'h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    ADDED_BOOK = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    ADDED_PRICE = (
        By.CSS_SELECTOR,
           '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')


