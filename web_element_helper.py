from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElementHelper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, by, locator):
        try:
            return self.wait.until(EC.presence_of_element_located((by, locator)))
        except Exception as e:
            print(f"Element not found: {locator} - {e}")
            return None

    def enter_text(self, by, locator, text):
        element = self.find_element(by, locator)
        if element:
            try:
                element.clear()
                element.send_keys(text)
                print(f"Entered text '{text}' in element: {locator}")
            except Exception as e:
                print(f"Failed to enter text: {e}")

    def click_element(self, by, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, locator)))
            element.click()
            print(f"Clicked element: {locator}")
        except Exception as e:
            print(f"Failed to click element: {e}")
