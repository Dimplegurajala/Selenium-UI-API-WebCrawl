from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    
    
    # Assertion Locators
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']") # The red error box
    PRODUCTS_HEADER = (By.CLASS_NAME, "title") # The 'Products' text on the next page

    def login(self, user, pwd):
        logger.info(f"Attempting login for: {user}")
        self.fill(self.USERNAME, user)
        self.fill(self.PASSWORD, pwd)
        self.click_element(self.LOGIN_BTN)
        logger.info("ACTION: Login button clicked")

    def is_login_successful(self):
        #Validates successful entry to the dashboard (PT).
        try:
            return self.wait_until_visible(self.PRODUCTS_HEADER).text == "Products"
        except:
            return False

    def get_error_message(self):
        #Captures the error text for Negative Testing (AT).
        return self.wait_until_visible(self.ERROR_CONTAINER).text

    