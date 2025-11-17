import pytest
from selenium import webdriver
import json
from pathlib import Path
import time
import pytest_html

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
    json_path = Path(__file__).resolve().parent.parent / "Data" / "my_data.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# TIME STAMP 
LOG_FILE = Path("test_stamps_web.log")

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
            
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" and report.failed:
        # Create screenshots directory inside the AutomacaoWeb package (next to this conftest)
        screenshots_dir = Path(__file__).resolve().parent / "screenshots_web"
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        # Take screenshot
        driver = item.funcargs['driver']
        screenshot_file = str(screenshots_dir / f"{item.name}_error.png")
        driver.save_screenshot(screenshot_file)
        # Add screenshot to the HTML report
        if screenshot_file:
            html = f'<div><img src="{screenshot_file}" alt="screenshot" style="width:304px;height:228px;" ' \
           f'onclick="window.open(this.src)" align="right"/></div>'
            extra.append(pytest_html.extras.html(html))
    report.extra = extra