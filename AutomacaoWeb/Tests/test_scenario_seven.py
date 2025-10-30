from Pages.menu_page import MenuPage
import pytest

@pytest.mark.usefixtures("load_data")
def test_scenario_seven(driver, load_data):
    menu_page = MenuPage(driver)
    
    # 1. Access the website: Open the browser and go to the Americanas website.
    menu_page.navigate()
    
    if menu_page.check_popup():
        menu_page.click_quit_popup()
        
    # 2. Navigate to Login: Click on the "Login or Sign Up" option.
    login_page = menu_page.click_login()
    
    # 3. Enter Incorrect Credentials: Fill in the email field with a valid user and enter an incorrect password.
    login_page.click_login_email_password()
    login_page.send_email(load_data["login"]["email"])
    login_page.send_password(load_data["login"]["incorrect_password"])
    
    # 4. Perform Login: Click the "Sign In" button.
    login_page.button_login_password()
    
    # 5. Validate Error: Verify that an appropriate error message (e.g., "Invalid email or password") is displayed and the login is not successful.
    assert login_page.validate_password_error_is_shown()