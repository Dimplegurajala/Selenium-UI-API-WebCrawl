from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Bootstrap Semantic Classes - elements which are prone to changes by dev
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BTNS = (By.CSS_SELECTOR, ".btn_inventory")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    
    # Sidebar for Logout
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def sort_by_text(self, text):
        #sorting logic.
        dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(text)

    def add_first_two_items(self):
        #Adds items to cart and returns names for validation
        btns = self.driver.find_elements(*self.ADD_TO_CART_BTNS)
        btns[0].click()
        btns[1].click()

    def open_cart(self):
        self.click_element(self.CART_LINK)

    def logout(self):
        #Prevents ghost sessions between tests.
        self.click_element(self.MENU_BTN)
        self.click_element(self.LOGOUT_LINK)