from appium.webdriver.common.appiumby import AppiumBy
from Pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Locators
        self.GRID_LIST_VIEW_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView[2]'
       
    def product_name(self, product):
        return f"//android.view.View[contains(@content-desc, '{product}')]"
     
    def get_product_name(self, product):
        xpath = self.product_name(product)
        prod = self.get_element_attribute(AppiumBy.XPATH, xpath)
        if "%" in prod:
            prod = prod.split('\n')[1]
            return prod
        else:
            prod = prod.split('\n')[0]
            return prod            
    
    def get_product_price(self, product):
        xpath = self.product_name(product)
        price = self.get_element_attribute(AppiumBy.XPATH, xpath)
        if "%" in price:
            price = price.split('\n')[3]
            price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
            return price
        else:
            price = price.split('\n')[1]
            price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
            return price
        
    # Click & Buttons
    def switch_list_grid(self):
        self.click_element(AppiumBy.XPATH, self.GRID_LIST_VIEW_XPATH)
        
    def click_product(self, product):
        from Pages.product_page import ProductPage
        xpath = self.product_name(product)
        self.click_element(AppiumBy.XPATH, xpath)
        return ProductPage(self.driver)
    
    # Validations
    def validate_product_name_is_shown_and_expected(self, product_name):
        return self.get_product_name(product_name) == product_name
    
    def validate_product_price_is_shown_and_expected(self, product_price,product_name):
        return self.get_product_price(product_name) == product_price