from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a'
        self.wait_timeout = 10  # Timeout in seconds
    
    def open(self):
        self.driver.get(self.url)
    
    def get_title(self):
        return self.driver.title
    
    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)
    
    def click_button_by_xpath(self, xpath):
        button = self.find_element_by_xpath(xpath)
        button.click()
    
    def wait_and_click_element_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, self.wait_timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            element.click()
        except Exception as e:
            print(f"Exception occurred: {str(e)}")

    def get_button_color_by_xpath(self, xpath):
        try:
            button = self.find_element_by_xpath(xpath)
            # Get computed style of the button using JavaScript
            return self.driver.execute_script(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');", button)
        except Exception as e:
            print(f"Exception occurred while getting button color: {str(e)}")
            return None