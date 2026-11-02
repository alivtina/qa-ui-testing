# UI Test Automation Portfolio

Automated browser testing of the SauceDemo web application using
Python, Playwright, and pytest.

## Test Coverage

- Successful login
- Locked-out user login
- Invalid username
- Invalid password
- Empty username
- Empty password
- Adding a product to the shopping cart

## Technologies

- Python
- Playwright
- pytest
- Chromium
- GitHub Actions

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```

## Test Results

7 automated UI tests passed locally in Chromium.

## Application Under Test

https://www.saucedemo.com/
