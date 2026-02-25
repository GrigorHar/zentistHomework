import re

import pytest
from playwright.sync_api import expect

from config.credentials import credentials
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


class TestScenario3LoginToSite:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.login_page = LoginPage(page)
        self.secure_page = SecurePage(page)
        self.login_page.goto()

    def test_login_with_valid_credentials_full_flow(self, page):
        if not credentials["username"] or not credentials["password"]:
            pytest.fail("LOGIN_USERNAME and LOGIN_PASSWORD must be set in .env")
        self.login_page.login(credentials["username"], credentials["password"])

        expect(page).to_have_url(r"/secure")

        title = self.secure_page.get_title()
        assert title
        assert len(title) > 0

        content = self.secure_page.get_page_content()
        assert "Secure Area" in content
        assert "Welcome to the Secure Area" in content

        expect(self.secure_page.get_logout_button()).to_be_visible()
        self.secure_page.get_logout_button().click()

        expect(page).to_have_url(r"/login")
        expect(self.login_page.get_flash_message()).to_contain_text(
            re.compile(r"logout|logged out", re.I)
        )
