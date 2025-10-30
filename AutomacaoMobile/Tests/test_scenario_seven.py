from Pages.home_page import HomePage
import pytest

@pytest.mark.usefixtures("load_data_mobile")
def test_scenario_seven(driver, load_data_mobile):
    home_page = HomePage(driver)
    data = load_data_mobile
    
    # 1. Access the website: Open the browser and go to the Americanas website.
    # 2. Navigate to Login: Click on the "Login or Sign Up" option.
    profile_page = home_page.click_profile()
    profile_page.click_login_email()
    login_page = profile_page.click_login_with_password()
    
    # 3. Enter Incorrect Credentials: Fill in the email field with a valid user and enter an incorrect password.
    login_page.send_email(data["login"]["email"])
    login_page.send_password(data["login"]["incorrect_password"])
    
    # 4. Perform Login: Click the "Sign In" button.
    login_page.login_button()
    
    # 5. Validate Error: Verify that an appropriate error message (e.g., "Invalid email or password") is displayed and the login is not successful.
    login_page.validate_password_error_is_shown()