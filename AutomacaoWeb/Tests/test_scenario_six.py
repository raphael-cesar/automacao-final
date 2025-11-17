from Pages.menu_page import MenuPage
import pytest
import time

@pytest.mark.usefixtures("load_data")
def test_scenario_six(driver, load_data):
    menu_page = MenuPage(driver)
    # 1. Access the website: Open the browser and go to the Americanas website.
    menu_page.navigate()
    
    # if menu_page.check_popup():
    #     menu_page.click_quit_popup()
        
    # 2. Navigate to Login: Click on the "Login or Sign Up" option.
    login_page = menu_page.click_login_page()
    
    # 3. Enter Correct Credentials: Fill in the fields with a valid and already registered email and password.
    login_page.click_login_email_password()
    login_page.send_email(load_data["login"]["email"])
    login_page.send_password(load_data["login"]["password"])
    
    # 4. Perform Login: Click the "Sign In" button.
    menu_page = login_page.button_login_password()
    
    # 5. Validate Login: Confirm the redirect to the homepage and that the user's email is displayed in the header.
    time.sleep(3) #Transition
    menu_page.validate_menu_is_shown()
    menu_page.validate_email_is_shown_and_expected(load_data["login"]["email"])