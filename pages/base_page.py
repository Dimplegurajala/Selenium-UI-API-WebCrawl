from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_clickable(self, locator, timeout=10):
        """Explicitly waits for an element to be ready for interaction."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        """Advanced click with intercept handling and Shadow DOM fallback."""
        try:
            element = self.wait_for_clickable(locator)
            element.click()
        except (TimeoutException, ElementClickInterceptedException):
            # Senior Fallback: If standard click fails, use JavaScript (Shadow DOM friendly)
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    def fill(self, locator, text):
        """Ensures visibility before interaction."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)