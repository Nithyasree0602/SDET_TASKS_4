from selenium.webdriver.common.by import By
from browser_manager import BrowserManager
from web_element_helper import WebElementHelper
import time

if __name__ == "__main__":
    
    browser = BrowserManager()
    driver = browser.driver
    if not driver:
        exit()

    browser.navigate_to("https://www.saucedemo.com/")
    helper = WebElementHelper(driver)
    helper.enter_text(By.ID, "user-name", "standard_user")
    helper.enter_text(By.ID, "password", "secret_sauce")
    helper.click_element(By.ID, "login-button")
    time.sleep(5)  
    browser.close_browser()
