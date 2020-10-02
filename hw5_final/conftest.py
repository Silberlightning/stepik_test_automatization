import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='None',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='None',
                     help="Choose GUI language for texts")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is None: raise pytest.UsageError("No language was submitted")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()
    else:
        print("Browser {} still is not implemented".format(browser_name))

    yield browser
    print("\nquit browser..")
    browser.quit()
