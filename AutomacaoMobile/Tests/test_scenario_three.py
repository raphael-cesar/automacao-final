from Pages.home_page import HomePage
from Tests_API.get import get_wishlist

def test_scenario_three(driver):
    data = get_wishlist()
    home_page = HomePage(driver)
    index = 0
    
    # Use the 3 products from wishlist projeto_final as an argument for loop execution
    for index in range(3):
        product_name = data[index]["Product"]  
        actual_price = data[index]["Price"]
        actual_price =  float(actual_price.replace(".", "").replace(",", ".").strip())
        invalid_zipcode = "00000001"
        
        # 1. Open App: Launch the Americanas application.
        if home_page.check_popup():
            home_page.close_popup()
            
        # 2. Search for Product: Use the search bar to look for a product from the wishlist.
        search_page = home_page.search_product(product_name)
        
        # 3. Select Product: Tap on the desired product in the search results.
        product_page = search_page.click_product(index)
        
        # 4. Validate Product Page:
        # Confirm that the product name and price are correct according to the API response.
        assert product_page.validate_product_name_is_shown_and_expected(product_name), f"Product API: {product_name}, Product NAME: {product_page.get_product_name()}"
        assert product_page.validate_product_price_is_shown_and_expected(actual_price, index), f"Price API:{actual_price}, Price PROD:{product_page.get_product_price(index)}"
        
        product_page.scroll("down")
        # Enter an invalid ZIP code, click "Calculate", and verify that an error message is displayed.
        product_page.search_zipcode(invalid_zipcode)
        assert product_page.validate_zipcode_error_alert_is_shown_and_expected()
        # Enter the valid ZIP code returned by the API and validate the delivery time and shipping cost.
        product_page.search_zipcode(data[index]["Zipcode"])
        
        # 5. Add to Cart: Tap the "Buy" button.
        # 6. Validate Cart Popup:
        # In the cart popup, confirm the product name and price again.
        # Increase the quantity to 2 and check if the quantity field is updated.
        # Decrease the quantity to 1 and check if the decrease button ( - ) becomes inactive.
        # Increase the quantity to 2 again.
        # 7. Add and go to cart: Proceed to the cart finalization screen.
        # 8. Validate Cart:
        # Confirm the product name and quantity.
        # Check if the total product value and the order subtotal are double the unit price.
        # Confirm that the value on the "Proceed to Checkout" button also reflects the total for two units.
        # Repeat the invalid and valid ZIP code test to ensure shipping calculation consistency.
        # 9. Proceed to Checkout: Tap "Proceed to Checkout".
        # 10. Validate Redirect: Check if the login/checkout screen is displayed with the message "Enter your email to continue".