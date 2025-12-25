import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# --- YOUR FIXTURE ---
@pytest.fixture(scope="function")
def driver(request): # Added 'request' to allow hook to access the driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    service = Service() 
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*.png", "*.jpg"]})
    driver.execute_cdp_cmd("Network.enable", {})

    yield driver
    
    try:
        driver.quit() 
    except Exception as e:
        print(f"Driver already dead: {e}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Use .get() to avoid KeyErrors if the driver didn't initialize
            driver = item.funcargs.get('driver')
            if driver:
                try:
                    screenshot = driver.get_screenshot_as_base64()
                    # Added 'alt' text and improved styling for the report
                    html = (f'<div><img src="data:image/png;base64,{screenshot}" '
                            f'alt="screenshot" style="width:300px;height:200px;border:1px solid red;" '
                            f'onclick="window.open(this.src)" align="right"/></div>')
                    extra.append(pytest_html.extras.html(html))
                except Exception as e:
                    print(f"Failed to capture base64 screenshot: {e}")
        report.extra = extra