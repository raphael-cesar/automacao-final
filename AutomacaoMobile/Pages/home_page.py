from Pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.PROFILE_PAGE_ACC_ID = "Conta\nTab 5 of 5"
        self.PROFILE_BANNER_XPATH = '//android.view.View[@content-desc="Perfil"]'
        self.SEARCH_BAR_XPATH = '//android.view.View[@content-desc="busque aqui seu produto"]'
        self.SEARCH_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView'
        
        self.BANNER_AD_XPATH = '//android.app.Dialog'
        self.CLOSE_BANNER_AD_ID = "wrap-close-button-1454703513201"
    
    # Getters
    def get_page_title(self):
        return self.get_element_text(AppiumBy.XPATH, self.PROFILE_BANNER_XPATH)
    
    def check_popup(self):
        return self.is_element_displayed(AppiumBy.XPATH, self.BANNER_AD_XPATH)
    
    #Buttons & Clicks
    def click_profile(self):
        from Pages.profile_page import ProfilePage
        self.click_element(AppiumBy.ACCESSIBILITY_ID, self.PROFILE_PAGE_ACC_ID)
        return ProfilePage(self.driver)
    
    # Senders
    def search_product(self, data):
        from Pages.search_page import SearchPage
        self.click_element(AppiumBy.XPATH, self.SEARCH_BAR_XPATH)
        self.send_keys_to_element(AppiumBy.XPATH, self.SEARCH_XPATH, data)
        self.enter_button()
        return SearchPage(self.driver)
    
    def close_popup(self):
        self.click_element(AppiumBy.ID, self.CLOSE_BANNER_AD_ID)
    
    # Validations
    def validate_menu_is_shown(self, expected_title):
        return self.get_page_title() == expected_title