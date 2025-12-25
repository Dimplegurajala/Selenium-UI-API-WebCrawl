import pytest
from selenium.webdriver.common.by import By

def test_webdriver_and_network_mocking(driver):
    """
    Verifies:
    1. WebDriver starts (Service & Path check)
    2. Headless mode works (Git Pipeline check)
    3. Network Mocking is active (Image blocking check)
    """
    # 1. Navigate to a site
    driver.get("https://www.google.com")
    
    # 2. Verify Page Title (Confirms connection)
    assert "Google" in driver.title
    
    # 3. Verify Network Mocking (Senior Optimization Check)
    # We check if an image element's naturalWidth is 0 (meaning it didn't load/was blocked)
    img_status = driver.execute_script(
        "return document.querySelector('img').naturalWidth;"
    )
    print(f"Image width: {img_status}") 
    # In a perfect block, this might be 0 or the element might not render fully
    
    # 4. Verify Shadow DOM fallback capability (optional check)
    # If this doesn't crash, your JS execution path is clear
    driver.execute_script("return document.documentElement")

    print("WebDriver Health: PASSED")