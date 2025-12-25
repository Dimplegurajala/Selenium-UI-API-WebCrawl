import pytest
from pages.login_page import LoginPage
from utils.data_helper import get_csv_data

# 1. Load the data
test_data = get_csv_data("users.csv")

# 2. Extract the test_id column (index 3) to use as labels in the report
@pytest.mark.parametrize(
    "user, pwd, expected, test_id", 
    test_data, 
    ids=[row[3] for row in test_data]  # This maps the 'test_id' to the report labels
)
def test_login_scenarios(driver, user, pwd, expected, test_id):
    login_pg = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    
    login_pg.login(user, pwd)
    
    # Logic remains clean and focused
    if expected == "success":
        assert "/inventory.html" in driver.current_url, f"Failed on: {test_id}"
    else:
        error_msg = login_pg.get_error_message()
        assert len(error_msg) > 0, f"Failed on: {test_id} - Error message not displayed"