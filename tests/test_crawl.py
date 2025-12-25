import os
import pytest
# Ensure this matches the folder 'pages' and file 'data_crawl'
from pages.data_crawl import SauceDemoCrawler

def test_saucedemo_inventory_crawl(driver):
    # 1. Login Logic
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    # 2. Use the imported class
    scraper = SauceDemoCrawler(driver)
    results = scraper.execute_crawl_and_save()
    
    # 3. Assertions
    assert len(results) > 0, "Crawl failed: No products found."
    assert os.path.exists('data/saucedemo_inventory.csv')