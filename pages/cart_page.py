from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    REMOVE_BTNS = (By.CSS_SELECTOR, ".cart_button")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BTN = (By.ID, "checkout")

    def remove_item(self):
        #Removes the first item from the cart.
        self.click_element(self.REMOVE_BTNS)

    def continue_shopping(self):
        self.click_element(self.CONTINUE_SHOPPING)

    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BTN)