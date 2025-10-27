import requests
import pytest

api_url = "http://127.0.0.1:8000/"

def test_api_run():
    resp = requests.get(f"{api_url}")
    assert resp.status_code == 200
    
def test_auth_user():
    load = {
        "email": "projeto@example.com",
        "password": "Senha123!"
    }
    resp = requests.post(f"{api_url}auth/login", json=load)
    resp = resp.json()
    access_token = resp.get("access_token")
    return access_token
    
def test_get_wishlist():
    HEADER = {
        'Authorization': f'Bearer {test_auth_user()}'
    }
    resp = requests.get(f"{api_url}/wishlists/1/products", headers=HEADER)
    assert resp.status_code == 200
    data = resp.json()
    return data

def test_1():
    data = test_get_wishlist()
    print(data[0]["Price"])
    