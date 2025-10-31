from appium.webdriver.common.appiumby import AppiumBy
from Pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Locators
        self.PRODUCT_NAME_XPATH = '(//android.widget.ScrollView//android.view.View[@content-desc])[1]'
        self.PRODUCT_PRICE_XPATH = '(//android.widget.ScrollView//android.view.View[@content-desc])[2]'
        self.PRODUCT_PRICE_APPLE_WATCH_XPATH = '(//android.widget.ScrollView//android.view.View[@content-desc])[4]'
        self.BACK_BUTTON_XPATH = '//android.widget.ImageView[@resource-id="Voltar"]'
        self.BACK_BUTTON_2_XPATH = '//android.view.View[@resource-id="Voltar"]'
        
        self.CANCEL_SEARCH_XPATH = '//android.view.View[@resource-id="Cancelar Busca"]/android.widget.ImageView'

    def back_menu(self):
        from Pages.home_page import HomePage
        self.click_element(AppiumBy.XPATH, self.BACK_BUTTON_XPATH)
        self.click_element(AppiumBy.XPATH, self.BACK_BUTTON_2_XPATH)
        self.click_element(AppiumBy.XPATH, self.CANCEL_SEARCH_XPATH) 
        return HomePage(self.driver) 
    
    # Getters
    def get_product_name(self):
        prod = self.get_element_attribute(AppiumBy.XPATH, self.PRODUCT_NAME_XPATH, "contentDescription")
        return prod
    
    def get_product_price(self, index):
        if index == 1 or index == 2:
            price = self.get_element_attribute(AppiumBy.XPATH, self.PRODUCT_PRICE_APPLE_WATCH_XPATH, "contentDescription")
            price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
            return price
        else:
            price = self.get_element_attribute(AppiumBy.XPATH, self.PRODUCT_PRICE_XPATH, "contentDescription")
            price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
            return price
    
    # Validations
    def validate_product_name_is_shown_and_expected(self, product_name):
        return self.get_product_name() == product_name
    
    def validate_product_price_is_shown_and_expected(self, product_price, index):
        return self.get_product_price(index) == product_price