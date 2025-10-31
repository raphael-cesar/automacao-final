from appium.webdriver.common.appiumby import AppiumBy
from Pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Locators
        self.GRID_LIST_VIEW_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView[2]'
        
        self.FIRST_PRODUCT_XPATH = "//android.widget.ScrollView/android.view.View"
        self.FIRST_PRODUCT_APPLE_WATCH_ACC_ID = "-12%\nApple Watch se gps Caixa prateada de alumínio – 44 mm Pulseira esportiva denim – p/m\n R$ 3.989,35\nR$ 3.529,00\nà vista"
        self.FIRST_PRODUCT_MACBOOK_ACC_ID = "-12%\nApple MacBook Air 13, M3, cpu de 8 núcleos, gpu de 8 núcleos, 24GB ram, 512GB ssd - Meia-noite\n R$ 21.055,35\nR$ 18.589,00\nà vista"
        
    def get_product_name(self, index):
        if index == 1:
            prod = self.get_element_attribute(AppiumBy.ACCESSIBILITY_ID, self.FIRST_PRODUCT_APPLE_WATCH_ACC_ID, "contentDescription")
            prod = prod.split('\n')[1]
            return prod
        elif index == 2:
            prod = self.get_element_attribute(AppiumBy.ACCESSIBILITY_ID, self.FIRST_PRODUCT_MACBOOK_ACC_ID, "contentDescription")
            prod = prod.split('\n')[1]
            return prod
        else:
            prod = self.get_element_attribute(AppiumBy.XPATH, self.FIRST_PRODUCT_XPATH, "contentDescription")
            prod = prod.split('\n')[0]
            return prod
    
    def get_product_price(self, index):
        if index == 1:
            price = self.get_element_attribute(AppiumBy.ACCESSIBILITY_ID, self.FIRST_PRODUCT_APPLE_WATCH_ACC_ID, "contentDescription")
            price = price.split('\n')[3]
            price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
            return price
        elif index == 2:
            price = self.get_element_attribute(AppiumBy.ACCESSIBILITY_ID, self.FIRST_PRODUCT_MACBOOK_ACC_ID, "contentDescription")
            price = price.split('\n')[3]
            price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
            return price
        else:
            price = self.get_element_attribute(AppiumBy.XPATH, self.FIRST_PRODUCT_XPATH, "contentDescription")
            price = price.split('\n')[1]
            price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
            return price
        
    # Click & Buttons
    def switch_list_grid(self):
        self.click_element(AppiumBy.XPATH, self.GRID_LIST_VIEW_XPATH)
        
    def click_product(self, index):
        from Pages.product_page import ProductPage
        if index == 1:
            self.click_element(AppiumBy.ACCESSIBILITY_ID, self.FIRST_PRODUCT_APPLE_WATCH_ACC_ID)
        elif index == 2:
            self.click_element(AppiumBy.ACCESSIBILITY_ID, self.FIRST_PRODUCT_MACBOOK_ACC_ID)
        else:
            self.click_element(AppiumBy.XPATH, self.FIRST_PRODUCT_XPATH)
        return ProductPage(self.driver)
    
    # Validations
    def validate_product_name_is_shown_and_expected(self, product_name, index):
        return self.get_product_name(index) == product_name
    
    def validate_product_price_is_shown_and_expected(self, product_price, index):
        return self.get_product_price(index) == product_price