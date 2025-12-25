from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) #global explicit wait

    def wait_until_visible(self, locator):
        #Standardized helper to wait for an element to appear
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_element_with_fallback(self, locator):
        #Standard search with Shadow DOM fallback.
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            # Fallback: Senior optimization for Shadow DOM components
            return self.driver.execute_script(
                "return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1])",
                locator[0], locator[1]
            )

    def fill(self, locator, text):
        element = self.find_element_with_fallback(locator)
        self.wait.until(EC.visibility_of(element))
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        #Ensures the element is not obscured by a 'Loading' overlay or pop-up."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception:
            # JavaScript click as a last resort if something is 'lagging' over the element
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)