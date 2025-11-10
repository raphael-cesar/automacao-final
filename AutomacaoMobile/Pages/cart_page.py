from Pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from logger import log
import re

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.SUBTOTAL_PRICE_XPATH = "//android.view.View[@content-desc='Subtotal']/following-sibling::android.view.View[1]"
        self.PROCEED_CHECKOUT_ID = '//android.view.View[contains(@content-desc, "fechar pedido")]'
        
        self.CART_ZIPCODE_XPATH = '//android.widget.EditText[@resource-id="Digite o CEP"]'
        self.CART_CALCULATE_ZIPCODE_XPATH = '//android.widget.Button[@content-desc="Calcular"]'
        self.EMAIL_TITLE_XPATH = '//android.view.View[@content-desc="Informe seu e-mail para continuar"]'
        self.ZIPCODE_ALERT_XPATH = '//android.widget.ImageView[@content-desc="Frete indisponível para o CEP: 00000-000"]'
        
        self.BACK_TO_CART_BUTTON_XPATH = '//android.widget.ImageView[@resource-id="Voltar"]'
        self.CLEAR_CART_BUTTON = '//android.view.View[@resource-id="Limpar carrinho"]'
        self.REMOVE_CONTINUE_BUTTON = '//android.widget.Button[@content-desc="Remover e continuar"]'
        self.CHOOSE_PRODUCT_XPATH = '//android.view.View[@resource-id="Escolher produtos"]'
        
    def product_name(self, product):
        return f"//android.widget.ImageView[contains(@content-desc, '{product}')]"
    
    def product_price(self, price):
        return f"//android.view.View[contains(@content-desc, '{price}')]"
    
    def product_quantity(self, quantity):
        return f'//android.widget.EditText[@text="{quantity}"]'
    
    def delivery_path(self, delivery):
        return f"//android.view.View[@content-desc='{delivery}']"
        
    
    # Getters
    def get_product_name(self, product):
        xpath = self.product_name(product)
        prod = self.get_element_attribute(AppiumBy.XPATH, xpath)
        return prod
    
    def get_product_value(self, value):
        xpath = self.product_price(value)
        price = self.get_element_attribute(AppiumBy.XPATH, xpath)
        price = price.split('\n')[-1]
        price = re.sub(r"[^0-9.,]", "", price)
        price = float(price.replace(".", "").replace(",", ".").replace(" ", "").strip())
        return price
    
    def get_product_quantity(self, quantity):
        xpath = self.product_quantity(quantity)
        return int(self.get_element_text(AppiumBy.XPATH, xpath))
    
    def get_subtotal_price(self):
        price = self.get_element_attribute(AppiumBy.XPATH, self.SUBTOTAL_PRICE_XPATH)
        price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
        return price
    
    def get_proceed_button_price(self):
        price = self.get_element_attribute(AppiumBy.XPATH, self.PROCEED_CHECKOUT_ID)
        price = price.split('\n')[1]
        price = float(price.replace("R$", "").replace(".", "").replace(",", ".").replace(" ", "").strip())
        return price
    
    def get_zipcode_error(self):
        return self.get_element_attribute(AppiumBy.XPATH, self.ZIPCODE_ALERT_XPATH)
    
    def get_delivery_fee(self, delivery):
        xpath = self.delivery_path(delivery)
        prod = self.get_element_attribute(AppiumBy.XPATH, xpath)
        return prod
    
    def get_email_title(self):
        return self.get_element_attribute(AppiumBy.XPATH, self.EMAIL_TITLE_XPATH)
    
    # Actions
    def search_zipcode(self, data):
        self.click_element(AppiumBy.XPATH, self.CART_ZIPCODE_XPATH)
        self.find_element(AppiumBy.XPATH, self.CART_ZIPCODE_XPATH).clear()
        self.send_keys_to_element(AppiumBy.XPATH, self.CART_ZIPCODE_XPATH, data)
        self.click_element(AppiumBy.XPATH, self.CART_CALCULATE_ZIPCODE_XPATH)
    
    # Click
    def click_proceed_button(self):
        self.click_element(AppiumBy.XPATH, self.PROCEED_CHECKOUT_ID)
    
    def back_to_cart(self):
        self.click_element(AppiumBy.XPATH, self.BACK_TO_CART_BUTTON_XPATH)
        
    def clear_cart(self):
        self.click_element(AppiumBy.XPATH, self.CLEAR_CART_BUTTON)
        
    def chose_product_button(self):
        self.click_element(AppiumBy.XPATH, self.CHOOSE_PRODUCT_XPATH)
        from Pages.product_page import ProductPage
        return ProductPage(self.driver)
        
    def click_remove_continue(self):
        self.click_element(AppiumBy.XPATH, self.REMOVE_CONTINUE_BUTTON)

    # Validations
    def validate_product_name_is_expected(self, product_name):
        return self.get_product_name(product_name) == product_name
    
    def validate_product_quantity_is_expected(self, product_quantity):
        return self.get_product_quantity(product_quantity) == product_quantity
    
    def validate_product_value_is_total_for_two_units(self, get_value, total_price):
        return self.get_product_value(get_value) == total_price
    
    def validate_product_subtotal_value_is_total_for_two_units(self, total_price):
        return self.get_subtotal_price() == total_price
    
    def validate_proceed_button_price_is_total_for_two_units(self, total_price):
        return self.get_proceed_button_price() == total_price
    
    def validate_zipcode_error_alert_is_shown_and_expected(self):
        return "Frete indisponível" in self.get_zipcode_error()
    
    def validate_delivery_fee_is_shown_and_expected(self, delivery ,delivery_fee):
        return delivery_fee in self.get_delivery_fee(delivery)
    
    def validate_delivery_time_is_shown_and_expected(self, delivery ,delivery_time):
        return delivery_time in self.get_delivery_fee(delivery)
    
    def validate_email_title_is_shown_and_expected(self):
        return self.get_email_title() == "Informe seu e-mail para continuar"