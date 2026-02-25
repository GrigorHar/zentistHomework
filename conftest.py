import os
from pathlib import Path

import dotenv
import pytest

dotenv.load_dotenv(Path(__file__).resolve().parent / ".env")

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "base_url": BASE_URL}


def pytest_configure(config):
    config.addinivalue_line("markers", "playwright: mark test as playwright test")

