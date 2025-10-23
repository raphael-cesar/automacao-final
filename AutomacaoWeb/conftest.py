import pytest
from selenium import webdriver
import json
from pathlib import Path

@pytest.fixture
def driver():
    # Setup: initialize the WebDriver
    driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    yield driver_instance
    # Teardown: close the WebDriver
    driver_instance.quit()
    
@pytest.fixture(scope="session")
def load_data():
    """Lê o JSON de capabilities e retorna como dicionário"""
    json_path = Path(__file__).resolve().parent / "Data" / "passwords.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data