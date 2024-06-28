from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # Initialize the Chrome driver once for all scenarios
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def after_scenario(context, scenario):
    # Quit the WebDriver after each scenario
    context.driver.quit()
