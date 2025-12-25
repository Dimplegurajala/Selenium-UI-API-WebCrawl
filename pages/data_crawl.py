import csv
import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

# Ensure the name is exactly SauceDemoCrawler
class SauceDemoCrawler(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_name = (By.CLASS_NAME, "inventory_item_name")
        self.product_price = (By.CLASS_NAME, "inventory_item_price")

    def execute_crawl_and_save(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.wait.until(EC.presence_of_all_elements_located(self.product_name))
        
        name_elements = self.driver.find_elements(*self.product_name)
        price_elements = self.driver.find_elements(*self.product_price)
        
        crawled_data = []
        for name, price in zip(name_elements, price_elements):
            crawled_data.append([name.text.strip(), price.text.strip()])

        os.makedirs('data', exist_ok=True)
        csv_path = 'data/saucedemo_inventory.csv'
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Product Name', 'Price'])
            writer.writerows(crawled_data)
            
        return crawled_data