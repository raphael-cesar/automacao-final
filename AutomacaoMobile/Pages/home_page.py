from Pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.PROFILE_PAGE_ACC_ID = "Conta\nTab 5 of 5"
        self.PROFILE_BANNER_XPATH = '//android.view.View[@content-desc="Perfil"]'
        
        self.BANNER_AD_ID = "wrap-close-button-1454703513201"
        self.BANNER_AD_CLASS = "android.app.Dialog"
        self.BANNER_AD_XPATH = '//android.app.Dialog'
    
    # Getters
    def get_page_title(self):
        return self.get_element_text(AppiumBy.XPATH, self.PROFILE_BANNER_XPATH)
    
    #Buttons & Clicks
    def click_profile(self):
        from Pages.profile_page import ProfilePage
        self.click_element(AppiumBy.ACCESSIBILITY_ID, self.PROFILE_PAGE_ACC_ID)
        return ProfilePage(self.driver)
    
    # Validations
    def validate_menu_is_shown(self, expected_title):
        return self.get_page_title() == expected_title