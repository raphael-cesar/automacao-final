from Pages.home_page import HomePage
import pytest

@pytest.mark.usefixtures("load_data_mobile")
def test_scenario_six(driver, load_data_mobile):
    home_page = HomePage(driver)
    data = load_data_mobile
    
    # 1. Access the website: Open the browser and go to the Americanas website.
    # if home_page.check_popup():
    #     home_page.close_popup()
        
    # 2. Navigate to Login: Click on the "Login or Sign Up" option.
    profile_page = home_page.click_profile()
    profile_page.click_login_email()
    login_page = profile_page.click_login_with_password()
    
    # 3. Enter Correct Credentials: Fill in the fields with a valid and already registered email and password.
    login_page.send_email(data["login"]["email"])
    login_page.send_password(data["login"]["password"])
    
    # 4. Perform Login: Click the "Sign In" button.
    home_page = login_page.login_button()
    
    # 5. Validate Login: Confirm the redirect to the homepage and that the user's email is displayed in the header.
    assert home_page.validate_menu_is_shown(data["login"]["email"])