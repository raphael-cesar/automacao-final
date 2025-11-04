import pytest
import json
from pathlib import Path
from appium import webdriver
from appium.options.common.base import AppiumOptions
import time

@pytest.fixture(scope="function")
def driver():
    # --- SETUP PHASE ---
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.b2w.americanas",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,  
        "appium:appWaitActivity": "com.b2w.americanas.MainActivity",
        "appium:autoGrantPermissions": True, 
        "appium: appWaitDuration": 5000,
    }) # Capabilities defined here
    _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    # The 'yield' keyword passes control to the test function
    yield _driver
    
    # --- TEARDOWN PHASE ---
    # This code runs AFTER the test function completes (or fails)
    
    print("\nQuitting driver...")
    # _driver.quit()

@pytest.fixture(scope="session")
def load_data_mobile():
    """Lê o JSON de capabilities e retorna como dicionário"""
    json_path = Path(__file__).resolve().parent.parent / "Data" / "my_data.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# TIME STAMP 
LOG_FILE = Path("test_durations_mobile.log")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    item.start_time = time.time()
    item.start_str = time.strftime("%H:%M:%S", time.localtime())
    msg = f"\n[START] Test '{item.nodeid}' - {item.start_str}"
    
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    duration = time.time() - item.start_time
    msg = f"[END] Test '{item.nodeid}' finished in {duration:.2f} seconds."

    # salva em arquivo
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")
        
@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # hookwrapper=True ensures pytest gives us the real test report
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":  # only after the test function runs
        result = "PASSED" if rep.failed is False else "FAILED"
        msg = f"[RESULT] Test '{item.nodeid}' -> {result}"
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(msg + "\n")