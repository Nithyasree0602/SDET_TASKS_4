from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

class BrowserManager:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.implicitly_wait(10)
            print("Chrome WebDriver initialized.")
        except WebDriverException as e:
            print("Error initializing WebDriver:", e)
            self.driver = None

    def navigate_to(self, url):
        if self.driver:
            try:
                self.driver.get(url)
                print(f"Navigated to {url}")
            except Exception as e:
                print(f"Failed to navigate to {url}: {e}")

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            print("Browser closed safely.")
