import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose GUI language for texts")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is None: raise pytest.UsageError("No language was submitted")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nstart browser for test..")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    yield browser

    print("\nquit browser..")
    browser.quit()
