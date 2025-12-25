import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    # integration of GIT-- CI/CD
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    #  bypassing 'Bot Detection' on sites
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    service = Service() 
    driver = webdriver.Chrome(service=service, options=options)
    
    # Performance Optimization: Blocks images to save bandwidth in CI
    # Comment these two lines out if the site requires images to render buttons!
    #driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*.png", "*.jpg", "*.jpeg", "*.gif"]})
    #driver.execute_cdp_cmd("Network.enable", {})

    yield driver
    
    try:
        driver.quit() 
    except Exception as e:
        print(f"Driver already dead: {e}")