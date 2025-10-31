from Pages.home_page import HomePage
from Tests_API.get import get_wishlist
import time

def test_scenario_five(driver):
    data = get_wishlist()
    home_page = HomePage(driver)
    index = 0
    
    # Use the 3 products from wishlist projeto_final as an argument for loop execution
    for index in range(3):
        # 1. Access Website/App: Open the Americanas website or app.
        if home_page.check_popup():
            home_page.close_popup()
            
        # 2. Search for Product: Search for a product that exists in your API Wishlist.
        search_page = home_page.search_product(data[index]["Product"])
        # 3. Validate Grid View: In the grid view, confirm that the product title and price are correct.
        prod_name = data[index]["Product"]
        actual_price = data[index]["Price"]
        actual_price =  float(actual_price.replace(".", "").replace(",", ".").strip())
        
        assert search_page.validate_product_name_is_shown_and_expected(data[index]["Product"]), f"Product API: {prod_name}, Product NAME: {search_page.get_product_name()}"
        print(search_page.validate_product_name_is_shown_and_expected(data[index]["Product"]))
        
        assert search_page.validate_product_price_is_shown_and_expected(actual_price), f"Price API:{actual_price}, Price PROD:{search_page.get_product_price()}"
        print(search_page.validate_product_price_is_shown_and_expected(actual_price))
        
        # 4. Validate List View: Switch to the list view and confirm the title and price again.
        # 5. Access Product Page: Click on the product to see its details.
        # 6. Validate Details Page: Confirm for the last time that the product title and price are correct.