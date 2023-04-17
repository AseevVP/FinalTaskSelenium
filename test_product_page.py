from .pages.product_page import ProductPage


def test_test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_the_basket()
    page.should_book_name_equals_hints_name()
    page.should_book_price_equals_hints_name()
