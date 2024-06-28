from behave import given, when, then
import time
from features.pages.homepage import HomePage

@when('visiting website')
def open_homepage(context):
    context.homepage = HomePage(context.driver)
    context.homepage.open()

@then('wait for {sec:d} seconds')
def wait_for_seconds(context, sec):
    time.sleep(sec)

@then('the title should be "{title}"')
def check_title(context, title):
    # Check if the page title matches the expected title
    assert context.homepage.get_title() == title, f"Expected title to be {title} but was {context.homepage.get_title()}"

@then('find element by xpath "{xpath}"')
def find_element_by_xpath(context, xpath):
    # Find the element specified by the XPath
    element = context.homepage.find_element_by_xpath(xpath)
    assert element is not None, f"Element with XPath {xpath} not found"

@then('click button by xpath "{xpath}"')
def click_button_by_xpath(context, xpath):
    # Click the button specified by the XPath
    context.homepage.click_button_by_xpath(xpath)

@then('waits until element is visible then clicks the element by xpath "{xpath}"')
def wait_and_click_element_by_xpath(context, xpath):
    # Waits until element is visible and clicks it by XPath
    context.homepage.wait_and_click_element_by_xpath(xpath)

@then('the button color should be "{expected_color}" for xpath "{xpath}"')
def check_button_color(context, expected_color, xpath):
    # Check if the button color matches the expected color
    actual_color = context.homepage.get_button_color_by_xpath(xpath)
    assert actual_color.lower() == expected_color.lower(), \
        f"Expected button color to be {expected_color} but was {actual_color}"