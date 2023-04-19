import time

import pytest

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


# def test_test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_the_basket()
#     page.should_book_name_equals_hints_name()
#     page.should_book_price_equals_hints_name()


# @pytest.mark.parametrize('link',
#                              ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                               pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_the_basket()
#     page.should_book_name_equals_hints_name()
#     page.should_book_price_equals_hints_name()
@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_the_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_the_basket()
    page.should_disappeared_success_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_form_into_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    page = BasketPage(browser, link)
    page.open()
    page.should_go_to_basket()
    time.sleep(10)
    page.should_verify_empty_basket_message()
    page.should_verify_empty_basket_content()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89'
    page = BasketPage(browser, link)
    page.open()
    page.should_go_to_basket()
    time.sleep(10)
    page.should_verify_empty_basket_message()
   # page.should_verify_empty_basket_content()
