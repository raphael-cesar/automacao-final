from appium.webdriver.common.appiumby import AppiumBy
from Pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Locators
        self.GRID_LIST_VIEW_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView[2]'
        self.FIRST_PRODUCT_ACC_ID = "//android.widget.ScrollView/android.view.View"
        
    def get_product_name(self):
        prod = self.get_element_attribute(AppiumBy.XPATH, self.FIRST_PRODUCT_ACC_ID, "contentDescription")
        prod = prod.split('\n')[0]
        return prod
    
    def get_product_price(self):
        price = self.get_element_attribute(AppiumBy.XPATH, self.FIRST_PRODUCT_ACC_ID, "contentDescription")
        price = price.split('\n')[1]
        price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
        return price
        
    # Validations
    def validate_product_name_is_shown_and_expected(self, product_name):
        return self.get_product_name() == product_name
    
    def validate_product_price_is_shown_and_expected(self, product_price):
        return self.get_product_price() == product_price
        