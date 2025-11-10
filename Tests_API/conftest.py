from pathlib import Path
import pytest
import time

# TIME STAMP 
LOG_FILE = Path("test_stamps_api.log")

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