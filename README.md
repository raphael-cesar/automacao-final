# Automation Tests - README

Short guide with project structure, how to run tests, virtualenv activation and how to view Allure results.

## Quick setup

1. (Optional) Use existing venv included in repo:
   - mac / linux:
     - source myproject/bin/activate
   - PowerShell:
     - & myproject/bin/Activate.ps1

   Or create a fresh venv:
   - python3 -m venv .venv
   - source .venv/bin/activate

2. Install dependencies:
```bash
# from repo root
pip install -r requirements.txt
```

## How to run tests

Run all tests (web + mobile + api)
```bash
pytest
```

Run only Web tests:
```bash
pytest AutomacaoWeb/Tests
```

Run only Mobile tests:
Ensure Appium server running at http://127.0.0.1:4723 and emulator/device available.
```bash
appium
```
```bash
pytest AutomacaoMobile/Tests
```

Run only API tests:
Ensurw internship-final-project-api server running at http://127.0.0.1:8000/
```bash
pytest Tests_API
```

Run a single test function:
```bash
pytest TestFolder/Tests/test_name.py
```

---

## Allure results

Pytest already writes Allure raw results to `allure-results/`

To view Allure report locally:

Serve report directly:
```bash
allure serve allure-results
```