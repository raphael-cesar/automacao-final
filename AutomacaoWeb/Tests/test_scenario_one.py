from Pages.menu_page import MenuPage
from Utils.data_loader import load_json_data
import time
import pytest

@pytest.mark.usefixtures("load_data")
def test_scenario_one(driver, load_data):
    menu_page = MenuPage(driver)
    
    menu_page.navigate()
    
    if menu_page.check_popup():
        menu_page.click_quit_popup()
        
    menu_page.click_login()
    
    email_page = menu_page.navigate_email()
    
    email_page.get_email()
    
    login_page = email_page.navigate_ame()
    
    actual_email = login_page.send_email()
    time.sleep(3)
    
    email_page = login_page.navigate_email()
    
    time.sleep(5)
    email_page.click_refresh()
    
    code = email_page.get_code()
    
    login_page = email_page.navigate_ame()
    
    menu_page = login_page.send_code(code)
    
    time.sleep(1)
    assert menu_page.validate_menu_is_shown()
    
    time.sleep(1)
    menu_page.get_header_email()
    
    assert menu_page.validate_email_is_shown_and_expected(actual_email), f"actual: {actual_email}, get_email:{menu_page.get_header_email()}"
    
    profile_page = menu_page.click_header_email()
    
    time.sleep(0.5)
    profile_page.click_auth()
    
    time.sleep(1)
    profile_page.click_set_password()
    
    email_page = profile_page.navigate_email()
    
    time.sleep(5)
    email_page.click_refresh()
    
    time.sleep(2)
    new_code = email_page.get_code()
    
    profile_page = email_page.navigate_profile()
    
    profile_page.send_code(new_code)

    profile_page.send_password(load_data["password_less_than_8"])
    assert not profile_page.validate_save_password_button()
    
    time.sleep(1)
    profile_page.clear_password_field()
    profile_page.send_password(load_data["password_without_numbers"])
    assert not profile_page.validate_save_password_button()
    
    time.sleep(1)
    profile_page.clear_password_field()
    profile_page.send_password(load_data["password_without_lowercase"])
    assert not profile_page.validate_save_password_button()
    
    time.sleep(1)
    profile_page.clear_password_field()
    profile_page.send_password(load_data["password_without_uppercase"])
    assert not profile_page.validate_save_password_button()
    
    time.sleep(1)
    profile_page.clear_password_field()
    profile_page.send_password(load_data["correct_password"])
    assert profile_page.validate_save_password_button()
    
    time.sleep(1)
    profile_page.click_save_password()
    assert profile_page.validate_mask_password_is_shown_and_expected()