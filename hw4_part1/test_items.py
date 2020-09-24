import locators as locators

def test_button_add_to_cart(browser):

    #Arrange
    browser.get(locators.link)
    search_input = browser.find_element_by_xpath(locators.search_input)

    #Act
    search_input.send_keys(locators.search_text)
    browser.find_element_by_css_selector(locators.button_search).click()

    #Assert
    button_to_cart = browser.find_element_by_xpath(locators.button).text
    assert len(button_to_cart) != 0, "Button text should not be null"

