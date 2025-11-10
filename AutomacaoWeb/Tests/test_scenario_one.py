from Pages.menu_page import MenuPage
import time
import pytest
import pyperclip

#@pytest.mark.repeat(10)
@pytest.mark.usefixtures("load_data")
def test_scenario_one(driver, load_data):
    menu_page = MenuPage(driver)
    
    # 1. Access the website: Open the browser and go to the Americanas website.
    menu_page.navigate()
    
    if menu_page.check_popup():
        menu_page.click_quit_popup()
    
    # 2. Navigate to Registration: Click on the "Login or Sign Up" option.
    menu_page.click_login()
    
    # 3. Generate Temporary Email: In a new tab, go to https://temp-mail.io/ and copy the generated email.
    email_page = menu_page.navigate_email()
    
    time.sleep(5)
    email_page.get_email()
    time.sleep(1)
    
    login_page = email_page.navigate_ame()
    
    # 4. Enter Email: Return to the Americanas website, enter the temporary email in the registration field, and click to send the verification code
    actual_email = pyperclip.paste()
    login_page.send_email(actual_email)
    login_page.button_login_code()
    time.sleep(3)
    
    
    email_page = login_page.navigate_email()
    
    time.sleep(5)
    email_page.click_refresh()
    
    #  5. Get Code: Go back to the temp-mail website, open the received email, and copy the verification code.
    code = email_page.get_code()
    
    # 6. Confirm Registration: Return to the Americanas website and enter the code to finalize the registration.
    login_page = email_page.navigate_ame()
    
    login_page.send_code(code)
    
    menu_page = login_page.click_send_code()
    
    # 7. Verify Redirect: Confirm that you have been redirected to the homepage.
    time.sleep(5) #Transition delay
    assert menu_page.validate_menu_is_shown()
    
    # 8. Validate Login: Check if the new user's email is displayed in the page header.
    
    menu_page.get_header_email()

    assert menu_page.validate_email_is_shown_and_expected(actual_email), f"actual: {actual_email}, get_email:{menu_page.get_header_email()}"
    
    # 9. Access My Account: Open the "My Account" menu and confirm that the email in the registration tab is correct.
    profile_page = menu_page.click_header_email()
    
    time.sleep(2)
    profile_page.click_auth()
    
    # 10. Start Password Setup: Navigate to the authentication section and select "Set Password".
    time.sleep(1)
    profile_page.click_set_password()
    
    # 11. Enter Password Code: Get the new code sent to temp-mail and enter it in the corresponding field.
    email_page = profile_page.navigate_email()
    
    time.sleep(5)
    email_page.click_refresh()
    
    time.sleep(2)
    new_code = email_page.get_code()
    
    profile_page = email_page.navigate_profile()
    
    profile_page.send_code(new_code)
    
    # 12. Test Password Rules:
    # Try to save a password with less than 8 characters. The "Save" button should be inactive.
    profile_page.send_password(load_data["passwords"]["password_less_than_8"])
    assert not profile_page.validate_save_password_button()
    
    # Try to save a password without numbers. The "Save" button should be inactive.
    time.sleep(1)
    profile_page.clear_password_field()
    profile_page.send_password(load_data["passwords"]["password_without_numbers"])
    assert not profile_page.validate_save_password_button()
    
    # Try to save a password without lowercase letters. The "Save" button should be inactive.
    time.sleep(1)
    profile_page.clear_password_field()
    profile_page.send_password(load_data["passwords"]["password_without_lowercase"])
    assert not profile_page.validate_save_password_button()
    
    # Try to save a password without uppercase letters. The "Save" button should be inactive.
    time.sleep(1)
    profile_page.clear_password_field()
    profile_page.send_password(load_data["passwords"]["password_without_uppercase"])
    assert not profile_page.validate_save_password_button()
    
    # 13. Set Valid Password: Enter a password that meets all criteria and click "Save Password".
    time.sleep(1)
    profile_page.clear_password_field()
    profile_page.send_password(load_data["passwords"]["correct_password"])
    assert profile_page.validate_save_password_button()
    
    time.sleep(1)
    profile_page.click_save_password()
    
    # 14. Validate success: Validate that the password was saved successfully (just validate that the sequence of asterisks appeared on the screen).
    assert profile_page.validate_mask_password_is_shown_and_expected()
    assert profile_page.validate_comma_is_shown()