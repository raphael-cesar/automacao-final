from Tests_API.get import get_wishlist
from Pages.menu_page import MenuPage

def test_scenario_five(driver):
    data = get_wishlist()
    menu_page = MenuPage(driver)
    index = 0
    # Use the 3 products from wishlist projeto_final as an argument for loop execution
    for index in range(3):
        # 1. Access Website/App: Open the Americanas website or app.
        menu_page.navigate()
    
        if menu_page.check_popup():
            menu_page.click_quit_popup()
            
        # 2. Search for Product: Search for a product that exists in your API Wishlist.
        menu_page.search_product(data[index]["Product"])
        search_page = menu_page.search()
        
        # 3. Validate Grid View: In the grid view, confirm that the product title and price are correct.
        json_price = data[index]["Price"]
        actual_price = float(json_price.replace(".", "").replace(",", ".").strip())        
            
        assert search_page.validate_product_name_is_shown_and_expected(data[index]["Product"])
        assert search_page.validate_product_price_is_shown_and_expected(actual_price),f"JSON Price:{json_price} & AME Price:{search_page.get_product_price()}"
        
        # 4. Validate List View: Switch to the list view and confirm the title and price again.
        search_page.switch_to_list_view()
        
        assert search_page.validate_product_name_is_shown_and_expected(data[index]["Product"])
        assert search_page.validate_product_price_is_shown_and_expected(actual_price),f"JSON Price:{json_price} & AME Price:{search_page.get_product_price()}"
        
        # 5. Access Product Page: Click on the product to see its details.
        product_page = search_page.click_product()
        
        # 6. Validate Details Page: Confirm for the last time that the product title and price are correct.
        assert product_page.validate_product_name_is_shown_and_expected(data[index]["Product"])
        assert product_page.validate_product_price_is_shown_and_expected(actual_price),f"JSON Price:{json_price} & AME Price:{search_page.get_product_price()}"
        
        product_page.return_driver()