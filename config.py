# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# def pytest_addoption(parser):
#     # parser.addoption('--browser_name', action='store', default='chrome',
#     #                  help="Choose browser: chrome or firefox")
#     parser.addoption('--language', action='store', default="en",
#                      help="Choose language: en or ru")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     # browser_name = request.config.getoption("browser_name")
#
#     user_language = request.config.getoption("language")
#     # browser = None
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#     browser = webdriver.Chrome(options=options)
#     # browser = None
#     # if user_language is not None:
#     #     print("\nstart chrome browser for test..")
#     #     browser = webdriver.Chrome(options=options)
#     # else:
#     #     raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     # print("\nquit browser..")
#     browser.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default=None,
        help='Specify your preferred language'
        )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if language is not None:
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language isn't specified")
    yield browser
    print("\nquit browser..")
    browser.quit()