import requests
from logger import log
from get import test_auth_user


api_url = "http://127.0.0.1:8000/"
register = "/auth/register"
login = "/auth/login"
wishlists = "/wishlists"

def test_scenario_eigth():
    new_user = {
        "email": "test@example.com",
        "password": "password123",
        "username": "testuser"
    }
    # Objective: Verify that a new user can be created successfully with a valid email and password.
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
    
def test_scenario_nine():
    # Objective: Ensure the API prevents registration with an email that is already in use.
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
    
def test_scenario_ten():
    # Objective: Test the API's validation for invalid input during registration.
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
    
def test_scenario_eleven():
    # Objective: Verify that a registered user can log in with correct credentials.
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

def test_scenario_twelve():
    # Objective: Ensure the API denies access if the password is incorrect.
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
    
def test_scenario_thirteen():
    # Objective: Ensure the API denies access if the user does not exist.
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
    
def test_scenario_fourteen():
    # Objective: Verify that an authenticated user can create a new wishlist.
    # Prerequisites: User must be authenticated (have a valid JWT token).
    access_token = test_auth_user()
    HEADER = {
        'Authorization': f'Bearer {access_token}'
    }
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
    
def test_scenario_fifteen():
    # Objective: Verify that a user can't create multiple wishlists with the same name.
    # Prerequisites: User must be authenticated.
    access_token = test_auth_user()
    HEADER = {
        'Authorization': f'Bearer {access_token}'
    }
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
    
def test_scenario_sixteen():