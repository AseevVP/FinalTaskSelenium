import pytest

from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        print('test1')

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        print('test2')


def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()


def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_register_form()
