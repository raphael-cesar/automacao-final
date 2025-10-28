from Pages.home_page import HomePage
import pytest

@pytest.mark.usefixtures("load_data_mobile")
def test_scenario_six(driver, load_data_mobile):
    home_page = HomePage(driver)
    data = load_data_mobile
    # 1. Access the website: Open the browser and go to the Americanas website.
    print(data["login"]["email"])
    # 2. Navigate to Login: Click on the "Login or Sign Up" option.
    # 3. Enter Correct Credentials: Fill in the fields with a valid and already registered email and password.
    # 4. Perform Login: Click the "Sign In" button.
    # 5. Validate Login: Confirm the redirect to the homepage and that the user's email is displayed in the header.