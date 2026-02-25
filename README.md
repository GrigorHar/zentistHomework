# Zentist - QA Automation

Playwright + pytest automation test suite for [The Internet](https://the-internet.herokuapp.com).

## Prerequisites

- Python 3.10 or higher
- pip

## Installation

```bash
pip install -r requirements.txt
python -m playwright install
```

**Required:** Create a `.env` file in the project root with `BASE_URL`, `LOGIN_USERNAME`, and `LOGIN_PASSWORD` before running tests (see [Credentials](#credentials)).

## Running Tests

### Run all tests

```bash
python -m pytest
```

### Run tests in headed mode (see browser)

```bash
python -m pytest --headed
```

### Run tests against a different environment

Set the `BASE_URL` environment variable:

```bash
# Windows (PowerShell)
$env:BASE_URL="https://staging.example.com"; python -m pytest

# Windows (CMD)
set BASE_URL=https://staging.example.com && python -m pytest

# Linux / macOS
BASE_URL=https://staging.example.com python -m pytest
```

### Run specific test file

```bash
python -m pytest tests/test_main_page.py
python -m pytest tests/test_login_invalid_credentials.py
python -m pytest tests/test_login_valid.py
```

### Run specific browser

```bash
python -m pytest --browser chromium
python -m pytest --browser firefox
python -m pytest --browser webkit
```

## Project Structure

```
zentist/
├── config/
│   └── credentials.py
├── pages/
│   ├── main_page.py
│   ├── login_page.py
│   └── secure_page.py
├── tests/
│   ├── test_main_page.py
│   ├── test_login_invalid_credentials.py
│   └── test_login_valid.py
├── conftest.py
├── requirements.txt
└── README.md
```

## Test Scenarios

### Scenario 1 - Main Page
- Open Main Page
- Assert page has title
- Assert page has 'Fork me on Github' element
- Assert page content contains 44 links

### Scenario 2 - Login Page (Invalid Credentials)
- Navigate from Main Page to Login Page via 'Form Authentication' link
- 14 test cases covering: empty credentials, wrong username/password, case sensitivity, SQL injection, special characters, whitespace, and similar-but-wrong passwords

### Scenario 3 - Login to the site
- Login with valid credentials (from `.env`)
- Assert user is on /secure page
- Assert page has title and content
- Assert page has "Logout" button
- Logout and assert user is logged out

## Credentials

**You must create a `.env` file** in the project root to run tests. All values are loaded from environment variables only (`.env` is not committed).

| Variable      | Description             | Required |
|---------------|-------------------------|----------|
| BASE_URL      | Application base URL    | No (default: the-internet.herokuapp.com) |
| LOGIN_USERNAME| Login username          | **Yes**  |
| LOGIN_PASSWORD| Login password          | **Yes**  |

Without `.env`, the login test will fail. Set `LOGIN_USERNAME`, `LOGIN_PASSWORD`, and optionally `BASE_URL` in your `.env` file.

### GitHub Actions

Add in **Settings → Secrets and variables → Actions**:

| Type     | Name           |
|----------|----------------|
| Secret   | LOGIN_USERNAME |
| Secret   | LOGIN_PASSWORD |
| Variable | BASE_URL (optional) |

## Test Data

| Valid credentials | Invalid            |
|-------------------|--------------------|
| Set via env vars  | Any other values   |
