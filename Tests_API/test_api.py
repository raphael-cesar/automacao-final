import requests
from logger import log

api_url = "http://127.0.0.1:8000/"
register = "/auth/register"
login = "/auth/login"
wishlists = "/wishlists"
my_wishlist = "/wishlists/1/products"

def get_header():
    new_user = {
        "email": "test@example.com",
        "password": "password123"
    }
    resp = requests.post(f"{api_url}{login}", json=new_user)
    resp = resp.json()
    new_access_token = resp.get("access_token")
    HEADER = {
        'Authorization': f'Bearer {new_access_token}'
    }
    return HEADER

def get_header_products():
    load = {
        "email": "projeto@example.com",
        "password": "Senha123!"
    }
    resp = requests.post(f"{api_url}{login}", json=load)
    resp = resp.json()
    access_token = resp.get("access_token")
    HEADER = {
        'Authorization': f'Bearer {access_token}'
    }
    return HEADER

def test_scenario_eigth(): # Objective: Verify that a new user can be created successfully with a valid email and password.
    new_user = {
        "email": "test@example.com",
        "password": "password123",
        "username": "testuser"
    }
    # Steps:
    # 1. Send a POST request to /auth/register .
    # 2. Provide a unique email (e.g., "testuser@example.com") and a strong password (e.g., "password123") in the request body.
    # Expected Result:
    resp = requests.post(f"{api_url}{register}", json=new_user)
    # The API should respond with a 200 OK status code.
    assert resp.status_code == 200
    # The response body should contain the user's data, including their ID and the email they registered with, but not the password.
    data = resp.json()
    log.info(f"ID:{data.get('id')}")
    log.info(f"Email:{data.get('email')}")
    
def test_scenario_nine(): # Objective: Ensure the API prevents registration with an email that is already in use.
    # Steps:
    # 1. First, register a user with a specific email (e.g., "existinguser@example.com").
    new_user = {
        "email": "test2@example.com",
        "password": "password123",
        "username": "testuser2"
    }
    new_user_2 = {
        "email": "test2@example.com",
        "password": "password123",
        "username": "testuser3"
    }
    # 2. Send a second POST request to /auth/register using the exact same email.
    # Expected Result:
    resp = requests.post(f"{api_url}{register}", json=new_user)
    assert resp.status_code == 200
    resp = requests.post(f"{api_url}{register}", json=new_user_2)
    assert resp.status_code == 400
    # The API should respond with a 400 Bad Request status code.
    # The response body should contain an error message indicating that the email is already registered (e.g., "Email already registered").
    data = resp.json()
    log.info(f"Error: {data.get('detail')}")
    
def test_scenario_ten(): # Objective: Test the API's validation for invalid input during registration.
    # Steps:
    new_user = {
        "email": "not-an-email",
        "password": "password123",
        "username": "testuser"
    }
    new_user_2 = {
        "email": "test2@example.com",
        "password": "",
        "username": "testuser2"
    }
    # 1. Send a POST request to /auth/register with an invalid email format (e.g., "not-an-email").
    resp = requests.post(f"{api_url}{register}", json=new_user)
    # The API should respond with a 422 Unprocessable Entity status code for both requests.
    assert resp.status_code == 422
    # 2. Send another request without a password field.
    resp_2 = requests.post(f"{api_url}{register}", json=new_user_2)
    # The API should respond with a 422 Unprocessable Entity status code for both requests.
    assert resp_2.status_code == 422
    # Expected Result:
    # The response body should detail the validation error (e.g., "value is not a valid email address" or "field required").
    resp = resp.json()
    resp_2 = resp_2.json()
    log.info(f"Email: {resp.get('detail')}")
    log.info(f"Password: {resp_2.get('detail')}")
    
def test_scenario_eleven(): # Objective: Verify that a registered user can log in with correct credentials.
    # Steps:
    # 1. Ensure a user is already registered (e.g., "loginuser@example.com" with password "correct_password").
    new_user = {
        "email": "loginuser@example.com",
        "password": "correct_password",
        "username": "testuser3"
    }
    resp = requests.post(f"{api_url}{register}", json=new_user)
    assert resp.status_code == 200
    
    # 2. Send a POST request to /auth/login using the registered email as the username and the correct password.
    resp = requests.post(f"{api_url}{login}", json=new_user)
    # Expected Result:
    # The API should respond with a 200 OK status code.
    assert resp.status_code == 200
    # The response body should contain an access_token (JWT) and a token_type of "bearer".
    resp = resp.json()
    access_token = resp.get("access_token")
    log.info(f"Token: {access_token}")

def test_scenario_twelve(): # Objective: Ensure the API denies access if the password is incorrect.
    # Steps:
    # 1. Use the credentials of a registered user (e.g., "loginuser@example.com").
    new_user = {
        "email": "loginuser2@example.com",
        "password": "correct_password",
        "username": "testuser4"
    }
    resp = requests.post(f"{api_url}{register}", json=new_user)
    assert resp.status_code == 200
    
    # 2. Send a POST request to /auth/login with the correct email but an incorrect password (e.g., "wrong_password").
    login_new_user = {
        "email": "loginuser@example.com",
        "password": "wrong_password",
    }
    resp = requests.post(f"{api_url}{login}", json=login_new_user)
    # Expected Result:
    # The API should respond with a 401 Unauthorized status code.
    assert resp.status_code == 401
    data = resp.json()
    # The response body should contain an error message like "Incorrect email or password".
    log.info(f"Error: {data.get('detail')}")
    
def test_scenario_thirteen(): # Objective: Ensure the API denies access if the user does not exist.
    # Steps:
    # 1. Send a POST request to /auth/login with an email that has not been registered (e.g., "nouser@example.com").
    login_new_user = {
        "email": "nouser@example.com",
        "password": "wrong_password",
    }
    resp = requests.post(f"{api_url}{login}", json=login_new_user)
    # Expected Result:
    # The API should respond with a 401 Unauthorized status code.
    assert resp.status_code == 401
    # The response body should contain an error message like "Incorrect email or password".
    data = resp.json()
    log.info(f"Error: {data.get('detail')}")
    
def test_scenario_fourteen(): # Objective: Verify that an authenticated user can create a new wishlist.
    # Prerequisites: User must be authenticated (have a valid JWT token).
    HEADER = get_header()
    new_wishlist = {
        "name": "My Tech Gadgets"
    }
    # Steps:
    # 1. Send a POST request to /wishlists with a valid authentication token in the header.
    # 2. Provide a name for the wishlist in the request body (e.g., {name": "My Tech Gadgets""} ).
    resp = requests.post(f"{api_url}{wishlists}", headers=HEADER, json=new_wishlist)
    # Expected Result:
    # The API should respond with a 200 OK status code.
    assert resp.status_code == 200
    data = resp.json()
    # The response body should contain the newly created wishlist object, including its id , name , and the owner_id .
    log.info(f"ID:{data.get('id')}")
    log.info(f"Email:{data.get('email')}")
    log.info(f"Owner id:{data.get('owner_id')}")
    
def test_scenario_fifteen(): # Objective: Verify that a user can't create multiple wishlists with the same name.
    # Prerequisites: User must be authenticated.
    HEADER = get_header()
    new_wishlist = {
        "name": "Travel Plans"
    }
    # Steps:
    # 1. Create a wishlist with a specific name (e.g., "Travel Plans").
    resp = requests.post(f"{api_url}{wishlists}", headers=HEADER, json=new_wishlist)
    assert resp.status_code == 200
    # 2. Send another POST request to /wishlists with the same name.
    resp = requests.post(f"{api_url}{wishlists}", headers=HEADER, json=new_wishlist)
    # Expected Result:
    # The API should respond with a 409 Conflict status code.
    assert resp.status_code == 409
    # A new wishlist should not be created with a different id .
    data = resp.json()
    log.info(f"Error: {data.get('message')}")
    
def test_scenario_sixteen(): # Objective: Ensure that an unauthenticated user cannot create a wishlist.
    new_wishlist = { 
        "name": "Travel Plans"
    }
    # Steps:
    # 1. Send a POST request to /wishlists without an authentication token.
    resp = requests.post(f"{api_url}{wishlists}", json=new_wishlist)
    # Expected Result:
    # The API should respond with a 401 Unauthorized status code.
    assert resp.status_code == 401
    # The response body should contain an error detail like "Not authenticated".
    data = resp.json()
    log.info(f"Error: {data.get('detail')}")
    
def test_scenario_seventeen(): # Objective: Test validation when creating a wishlist with no name.
    # Prerequisites: User must be authenticated.  
    HEADER = get_header()
    new_wishlist = {}
    # Steps:
    # 1. Send a POST request to /wishlists with an empty request body {} .
    resp = requests.post(f"{api_url}{wishlists}", headers=HEADER, json=new_wishlist)
    # Expected Result:
    # The API should respond with a 422 Unprocessable Entity status code.
    assert resp.status_code == 422
    # The response should detail the validation error (e.g., "field required").
    data = resp.json()
    log.info(f"Error: {data.get('detail')}")
    
def test_scenario_eighteen(): # Objective: Verify that an authenticated user can retrieve all of their wishlists.
    # Prerequisites: User must be authenticated and have one or more wishlists.
    HEADER = get_header()
    # Steps:
    # 1. Send a GET request to /wishlists with a valid authentication token.
    resp = requests.get(f"{api_url}{wishlists}", headers=HEADER)
    # Expected Result:
    # The API should respond with a 200 OK status code.
    assert resp.status_code == 200
    # The response body should be a JSON array containing all wishlists owned by the user
    data = resp.json()
    log.info(data)
    
def test_scenario_nineteen(): # Objective: Verify the response when a user has no wishlists.
    # Prerequisites: User must be authenticated but have no wishlists created.
    new_user = {
        "email": "projeto2@example.com",
        "password": "Senha123!",
        "username": "testuser5"
    }
    resp = requests.post(f"{api_url}{register}", json=new_user)
    assert resp.status_code == 200
    
    resp = requests.post(f"{api_url}{login}", json=new_user)
    assert resp.status_code == 200
    resp = resp.json()
    new_access_token = resp.get("access_token")
    
    new_HEADER = {
        'Authorization': f'Bearer {new_access_token}'
    }
    # Steps:
    # 1. Send a GET request to /wishlists with a valid authentication token.
    resp = requests.get(f"{api_url}{wishlists}", headers=new_HEADER)
    # Expected Result:
    # The API should respond with a 200 OK status code.
    assert resp.status_code == 200
    # The response body should be an empty JSON array [] .
    data = resp.json()
    log.info(data)
    
def test_scenario_twenty():
    # Objective: Ensure an unauthenticated user cannot retrieve wishlists.
    # Steps:
    # 1. Send a GET request to /wishlists without an authentication token.
    resp = requests.get(f"{api_url}{wishlists}")
    # Expected Result:
    # The API should respond with a 401 Unauthorized status code.
    assert resp.status_code == 401
    log.info(f"Error: {resp.status_code}")
    
    
def test_scenario_twenty_one(): # Objective: Verify that a product can be added to a specific wishlist.
    # Prerequisites: User is authenticated and owns a wishlist (e.g., with id=1 ).
    HEADER = get_header()
    
    new_wishlist = {
        "name": "Wishlist"
    }
    resp = requests.post(f"{api_url}{wishlists}", headers=HEADER ,json=new_wishlist)
    assert resp.status_code == 200
    wishlist_id = resp.json().get("id")
    
    resp = requests.get(f"{api_url}{wishlists}", headers=HEADER)
    assert resp.status_code == 200
    data = resp.json()
    log.info(data)

    # Steps:
    # 1. Send a POST request to /wishlists/1/products with a valid auth token.
    # 2. Provide valid product data in the request body: {"Product": "New Gadget", "Price": "99.99", "Zipcode": "12345678"} .
    new_product = {
        "Product": "New Gadget", "Price": "99.99", "Zipcode": "12345678", "delivery_estimate": "5 days","shipping_fee": "2.00"
    }
    resp = requests.post(f"{api_url}/wishlists/{wishlist_id}/products", headers=HEADER, json=new_product)
    # Expected Result:
    # The API should respond with a 200 OK status code.
    assert resp.status_code == 200
    # The response body should contain the created product object, including its new id and the wishlist_id .
    data = resp.json()
    log.info(data)  
    # The is_purchased field should be false .
    assert data["is_purchased"] == False
    
def test_scenario_twenty_two(): # Objective: Ensure a product cannot be added to a wishlist that does not exist.
    # Prerequisites: User is authenticated.
    HEADER = get_header()
    # Steps:
    # 1. Send a POST request to /wishlists/999/products (where 999 is a non-existent ID) with a valid auth token and product data.
    new_product = {
        "Product": "New Gadget", "Price": "99.99", "Zipcode": "12345678","delivery_estimate": "5 days","shipping_fee": "2.00"
    }
    resp = requests.post(f"{api_url}/wishlists/999/products", headers=HEADER, json=new_product)
    # Expected Result:
    # The API should respond with a 404 Not Found status code.
    assert resp.status_code == 404
    # The response body should contain an error message like "Wishlist not found".
    data = resp.json()
    log.info(f"{data.get('detail')}")
    
def test_scenario_twenty_three(): # Objective: Ensure a user cannot add a product to a wishlist they do not own.
    # Prerequisites: Two users exist. User A owns wishlist 1. User B is authenticated.
    user_A = {
        "email": "user_a@example.com",
        "password": "Senha123!",
        "username": "testuser7"
    }
    resp = requests.post(f"{api_url}{register}", json=user_A)
    assert resp.status_code == 200
    
    resp = requests.post(f"{api_url}{login}", json=user_A)
    assert resp.status_code == 200
    resp = resp.json()
    access_token_user_a = resp.get("access_token")
    
    HEADER_USER_A = {
        'Authorization': f'Bearer {access_token_user_a}'
    }
    new_wishlist = {
        "name": "Wishlist"
    }
    resp = requests.post(f"{api_url}{wishlists}", headers=HEADER_USER_A ,json=new_wishlist)
    assert resp.status_code == 200
    wishlist_id = resp.json().get("id")
    
    user_B = {
        "email": "user_b@example.com",
        "password": "Senha123!",
        "username": "testuser8"
    }
    resp = requests.post(f"{api_url}{register}", json=user_B)
    assert resp.status_code == 200
    resp = requests.post(f"{api_url}{login}", json=user_B)
    assert resp.status_code == 200
    resp = resp.json()
    access_token_user_b = resp.get("access_token")
    HEADER_USER_B = {
        'Authorization': f'Bearer {access_token_user_b}'
    }
    
    # Steps:
    # 1. User B sends a POST request to /wishlists/1/products with their auth token.
    new_product = {
        "Product": "New Gadget", "Price": "99.99", "Zipcode": "12345678","delivery_estimate": "5 days","shipping_fee": "2.00"
    }
    resp = requests.post(f"{api_url}/wishlist/{wishlist_id}/products", headers=HEADER_USER_B, json=new_product)
    # Expected Result:
    # The API should respond with a 404 Not Found status code (as the wishlist is not found for that specific user).
    assert resp.status_code == 404
    log.info(f"Error: {resp.status_code}")
    
def test_scenario_twenty_four(): # Objective: Test validation when required product fields are missing.
    # Prerequisites: User is authenticated and owns a wishlist.
    HEADER = get_header()
    new_product = {
        "Product": "New Gadget", "Zipcode": "12345678","delivery_estimate": "5 days","shipping_fee": "2.00"
    }
    resp = requests.get(f"{api_url}{wishlists}", headers=HEADER)
    wishlist_id = resp.json()[0]["id"]
    # Steps:
    # 1. Send a POST request to /wishlists/1/products with missing required fields (e.g., {"Price": "10.00"} ).
    resp = requests.post(f"{api_url}/wishlists/{wishlist_id}/products", headers=HEADER, json=new_product)
    # Expected Result:
    # The API should respond with a 422 Unprocessable Entity status code.
    assert resp.status_code == 422
    # The response should detail the missing fields.
    data = resp.json()
    log.info(f"Error: {data.get('detail')}")
    
def test_scenario_twenty_five(): # Objective: Verify that all products from a specific wishlist can be retrieved.
    # Prerequisites: User is authenticated and owns a wishlist with products.
    HEADER = get_header_products()
    # Steps:
    # 1. Send a GET request to /wishlists/1/products with a valid auth token.
    resp = requests.get(f"{api_url}{my_wishlist}", headers=HEADER)
    # Expected Result:
    # The API should respond with a 200 OK status code.
    assert resp.status_code == 200
    # The response body should be a JSON array of product objects belonging to that wishlist.
    data = resp.json()
    log.info(data)
    
def test_scenario_twenty_six(): # Objective: Test filtering products by name.
    # Prerequisites: User is authenticated and owns a wishlist with a product named "Apple iPhone".
    HEADER = get_header_products()
    # Steps:
    # 1. Send a GET request to /wishlists/1/products?Product=iPhone with a valid auth token.
    resp = requests.get(f"{api_url}{my_wishlist}?Product=iPhone", headers=HEADER)
    # Expected Result:
    # The API should respond with a 200 OK status code.
    assert resp.status_code == 200
    # The response body should contain only products whose name contains "iPhone".
    data = resp.json()
    log.info(data)
    
def test_scenario_twenty_seven():   # Objective: Test filtering products by their purchased status.
    # Prerequisites: User is authenticated and owns a wishlist with purchased and unpurchased items.
    HEADER = get_header()
    new_product = {
        "Product": "New Gadget","Price": "99.99", "Zipcode": "12345678","delivery_estimate": "5 days","shipping_fee": "2.00", "is_purchased": True
    }
    super_new_product = {
        "Product": "Super New Gadget","Price": "99.99", "Zipcode": "12345678","delivery_estimate": "5 days","shipping_fee": "2.00"
    }
    super_hiper_new_product = {
        "Product": "Super Hiper New Gadget","Price": "99.99", "Zipcode": "12345678","delivery_estimate": "5 days","shipping_fee": "2.00"
    }
    resp = requests.get(f"{api_url}{wishlists}", headers=HEADER)
    wishlist_id = resp.json()[0]["id"]
    
    resp = requests.post(f"{api_url}/wishlists/{wishlist_id}/products", headers=HEADER, json=new_product)
    product_id = resp.json()["id"]
    
    requests.post(f"{api_url}/wishlists/{wishlist_id}/products", headers=HEADER, json=super_new_product)
    requests.post(f"{api_url}/wishlists/{wishlist_id}/products", headers=HEADER, json=super_hiper_new_product)
    
    new_product_purchased = {
        "is_purchased": True
    }
    
    resp = requests.put(f"{api_url}/products/{product_id}", headers=HEADER, json=new_product_purchased)
    assert resp.status_code == 200
    
    # Steps:
    # 1. Send a GET request to /wishlists/1/products?is_purchased=true .
    resp = requests.get(f"{api_url}/wishlists/{wishlist_id}/products?is_purchased=true", headers=HEADER)
    # Expected Result:
    # The API should respond with a 200 OK status code.
    assert resp.status_code == 200
    # The response body should only contain products that have been marked as purchased.
    data = resp.json()
    log.info(data)

def test_scenario_twenty_eight():# Objective: Ensure a user cannot view products from a wishlist they do not own.
    
    HEADER_USER_A = get_header_products()
    new_wishlist = {
        "name": "Wishlist"
    }
    
    resp = requests.post(f"{api_url}{wishlists}", headers=HEADER_USER_A ,json=new_wishlist)
    assert resp.status_code == 200
    
    user_B = {
        "email": "user_b@example.com",
        "password": "Senha123!",
    }
    resp = requests.post(f"{api_url}{login}", json=user_B)
    assert resp.status_code == 200
    resp = resp.json()
    access_token_user_b = resp.get("access_token")
    HEADER_USER_B = {
        'Authorization': f'Bearer {access_token_user_b}'
    }
    
    # Prerequisites: User A owns wishlist 1. User B is authenticated.
    # Steps:
    # 1. User B sends a GET request to /wishlists/1/products with their auth token.
    resp = requests.get(f"{api_url}/wishlist/1/products", headers=HEADER_USER_B)
    # Expected Result:
    # The API should respond with a 404 Not Found status code.
    assert resp.status_code == 404
    log.info(f"Error: {resp.status_code}")
    
def test_scenario_twenty_nine(): # Objective: Verify that a product's details can be updated.
    # Prerequisites: User is authenticated and owns a product (e.g., with id=1 ).
    HEADER = get_header_products()
    
    # 2. Provide the fields to be updated in the request body (e.g., {"Price": "150.00"} ).
    new_price = {"Price": "150.00"}
    # Steps:
    # 1. Send a PUT request to /products/1 with a valid auth token.
    resp = requests.put(f"{api_url}products/1", headers=HEADER, json=new_price)
    
    # Expected Result:
    # The API should respond with a 200 OK status code.
    assert resp.status_code == 200
    # The response body should contain the full product object with the updated price.
    data = resp.json()
    log.info(data)
    
def test_scenario_thirty(): # Objective: Ensure an error is returned when trying to update a non-existent product.
    # Prerequisites: User is authenticated.
    HEADER = get_header_products()
    new_price = {"Price": "150.00"}
    # Steps:
    # 1. Send a PUT request to /products/999 with an auth token and update data.
    resp = requests.put(f"{api_url}products/999", headers=HEADER, json=new_price)
    # Expected Result:
    # The API should respond with a 404 Not Found status code.
    assert resp.status_code == 404
    log.info(f"Error: {resp.status_code}")
    
def test_scenario_thirty_one(): # Objective: Ensure a user cannot update a product they do not own.
    # Prerequisites: User A owns product 1. User B is authenticated.
    HEADER_USER_A = get_header_products()
    resp = requests.get(f"{api_url}{my_wishlist}", headers=HEADER_USER_A)
    assert resp.status_code == 200
    
    user_B = {
        "email": "user_b@example.com",
        "password": "Senha123!",
    }
    resp = requests.post(f"{api_url}{login}", json=user_B)
    assert resp.status_code == 200
    resp = resp.json()
    access_token_user_b = resp.get("access_token")
    HEADER_USER_B = {
        'Authorization': f'Bearer {access_token_user_b}'
    }
    # Steps:
    # 1. User B sends a PUT request to /products/1 with their auth token.
    new_price = {"Price": "150.00"}
    resp = requests.put(f"{api_url}/products/1", headers=HEADER_USER_B, json=new_price)
    
    # Expected Result:
    # The API should respond with a 404 Not Found status code.
    assert resp.status_code == 404
    log.info(f"Error: {resp.status_code}")
    
def test_scenario_thirty_two(): # Objective: Verify that a product can be deleted from a wishlist.
    # Prerequisites: User is authenticated and owns a product (e.g., with id=1 ).
    HEADER = get_header_products()
    # Steps:
    # 1. Send a DELETE request to /products/1 with a valid auth token.
    resp = requests.delete(f"{api_url}products/1", headers=HEADER)
    # Expected Result:
    # The API should respond with a 204 No Content status code.
    assert resp.status_code == 204
    
def test_scenario_thirty_three(): # Objective: Ensure an error is returned when trying to delete a non-existent product.
    # Prerequisites: User is authenticated.
    HEADER = get_header_products()
    # Steps:
    # 1. Send a DELETE request to /products/999 with an auth token.
    resp = requests.delete(f"{api_url}products/999", headers=HEADER)
    # Expected Result:
    # The API should respond with a 404 Not Found status code.
    assert resp.status_code == 404
    data = resp.json()
    log.info(f"Error: {data.get('detail')}")
    
def test_scenario_thirty_four(): # Objective: Ensure a user cannot delete a product they do not own.
    # Prerequisites: User A owns product 1. User B is authenticated.
    HEADER_USER_A = get_header_products()
    resp = requests.get(f"{api_url}{my_wishlist}", headers=HEADER_USER_A)
    assert resp.status_code == 200
    
    user_B = {
        "email": "user_b@example.com",
        "password": "Senha123!",
    }
    resp = requests.post(f"{api_url}{login}", json=user_B)
    assert resp.status_code == 200
    resp = resp.json()
    access_token_user_b = resp.get("access_token")
    HEADER_USER_B = {
        'Authorization': f'Bearer {access_token_user_b}'
    }
    # Steps:
    # 1. User B sends a DELETE request to /products/1 with their auth token.
    resp = requests.delete(f"{api_url}/products/1", headers=HEADER_USER_B)
    # Expected Result:
    # The API should respond with a 404 Not Found status code.
    assert resp.status_code == 404
    
def test_scenario_thirty_five(): # Objective: Verify that all endpoints requiring authentication return a 401 Unauthorized error when no token is provided.
    # 1. For each endpoint, send a request without the Authorization header.
    # Endpoints to Test:
    # POST /wishlists
    new_wishlist = {
        "name": "Teste"
    }
    resp = requests.post(f"{api_url}/wishlists", json=new_wishlist)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error POST WISHLIST: {data.get('detail')}")
    
    # GET /wishlists
    resp = requests.get(f"{api_url}/wishlists")
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error GET WISHLIST: {data.get('detail')}")
    
    # POST /wishlists/{wishlist_id}/products
    new_product = {
        "Product": "New Gadget","Price": "99.99", "Zipcode": "12345678","delivery_estimate": "5 days","shipping_fee": "2.00", "is_purchased": True
    }
    resp = requests.post(f"{api_url}/wishlists/1/products", json=new_product)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error POST /wishlists/1/products: {data.get('detail')}")
    
    # GET /wishlists/{wishlist_id}/
    resp = requests.get(f"{api_url}/wishlists/1/products")
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error GET /wishlists/1/: {data.get('detail')}")
    
    # PUT /products/{product_id}
    new_price = {"Price": "150.00"}
    resp = requests.put(f"{api_url}/products/1", json=new_price)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error PUT /products/1: {data.get('detail')}")
    
    # DELETE /products/{product_id}
    resp = requests.delete(f"{api_url}/products/1")
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error DELETE /products/1: {data.get('detail')}")
    
    # PATCH /products/{product_id}/toggle
    resp = requests.patch(f"{api_url}/products/1/toggle", json=new_price)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error PATCH /products/1/toggle: {data.get('detail')}")
    
def test_scenario_thirty_six(): # Objective: Verify that all endpoints requiring authentication return a 401 Unauthorized error when an invalid, malformed, or expired token is provided.
    # A completely invalid string (e.g., "Bearer invalidtoken").
    # A correctly formatted but expired JWT.
    # A token signed with a different secret key.
    # 1. For each endpoint, send a request with an Authorization header containing a token that is either:
    new_user = {
        "email": "test@example.com",
        "password": "password123"
    }
    resp = requests.post(f"{api_url}{login}", json=new_user)
    resp = resp.json()
    new_access_token = resp.get("access_token")
    HEADER = {
        'Authorization': f'Bearer {new_access_token+"invalido"}'
    }
    
    # Endpoints to Test:
    # POST /wishlists
    new_wishlist = {
        "name": "Teste"
    }
    resp = requests.post(f"{api_url}/wishlists", headers=HEADER , json=new_wishlist)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error POST WISHLIST: {data.get('detail')}")
    
    # GET /wishlists
    resp = requests.get(f"{api_url}/wishlists/1/products", headers=HEADER)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error GET /wishlists/1/: {data.get('detail')}")
    
    # POST /wishlists/{wishlist_id}/products
    new_product = {
        "Product": "New Gadget","Price": "99.99", "Zipcode": "12345678","delivery_estimate": "5 days","shipping_fee": "2.00", "is_purchased": True
    }
    resp = requests.post(f"{api_url}/wishlists/1/products", headers=HEADER, json=new_product)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error POST /wishlists/1/products: {data.get('detail')}")
    
    # GET /wishlists/{wishlist_id}/
    resp = requests.get(f"{api_url}/wishlists/1/products", headers=HEADER)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error GET /wishlists/1/: {data.get('detail')}")
    
    # PUT /products/{product_id}
    new_price = {"Price": "150.00"}
    resp = requests.put(f"{api_url}/products/1", headers=HEADER, json=new_price)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error PUT /products/1: {data.get('detail')}")
    
    # DELETE /products/{product_id}
    resp = requests.delete(f"{api_url}/products/1", headers=HEADER)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error DELETE /products/1: {data.get('detail')}")
    
    # PATCH /products/{product_id}/toggle
    resp = requests.patch(f"{api_url}/products/1/toggle", headers=HEADER, json=new_price)
    assert resp.status_code == 401
    data = resp.json()
    log.info(f"Error PATCH /products/1/toggle: {data.get('detail')}")