import re

import pytest
from playwright.sync_api import expect

from config.credentials import credentials
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestScenario2LoginPageInvalidCredentials:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.main_page = MainPage(page)
        self.login_page = LoginPage(page)
        self.main_page.goto()
        self.main_page.click_form_authentication()

    def _assert_invalid_login(self, page, username: str, password: str):
        self.login_page.login(username, password)
        expect(self.login_page.get_flash_message()).to_be_visible()
        expect(self.login_page.get_flash_message()).to_contain_text(
            "invalid", ignore_case=True
        )
        expect(page).to_have_url(re.compile(r"/login$"))

    def test_empty_username_and_empty_password_cannot_login(self, page):
        self._assert_invalid_login(page, "", "")

    def test_valid_username_wrong_password_cannot_login(self, page):
        if not credentials["username"]:
            pytest.skip("LOGIN_USERNAME required")
        self._assert_invalid_login(page, credentials["username"], "WrongPassword")

    def test_wrong_username_valid_password_cannot_login(self, page):
        if not credentials["password"]:
            pytest.skip("LOGIN_PASSWORD required")
        self._assert_invalid_login(page, "wronguser", credentials["password"])

    def test_wrong_username_wrong_password_cannot_login(self, page):
        self._assert_invalid_login(page, "invaliduser", "invalidpass")

    def test_empty_username_valid_password_cannot_login(self, page):
        if not credentials["password"]:
            pytest.skip("LOGIN_PASSWORD required")
        self._assert_invalid_login(page, "", credentials["password"])

    def test_valid_username_empty_password_cannot_login(self, page):
        if not credentials["username"]:
            pytest.skip("LOGIN_USERNAME required")
        self._assert_invalid_login(page, credentials["username"], "")

    def test_case_sensitive_wrong_username_case_cannot_login(self, page):
        if not credentials["username"] or not credentials["password"]:
            pytest.skip("LOGIN_USERNAME and LOGIN_PASSWORD required")
        wrong_case = credentials["username"].swapcase()
        self._assert_invalid_login(page, wrong_case, credentials["password"])

    def test_case_sensitive_wrong_password_case_cannot_login(self, page):
        if not credentials["username"] or not credentials["password"]:
            pytest.skip("LOGIN_USERNAME and LOGIN_PASSWORD required")
        wrong_case = credentials["password"].lower()
        self._assert_invalid_login(page, credentials["username"], wrong_case)

    def test_whitespace_only_username_cannot_login(self, page):
        if not credentials["password"]:
            pytest.skip("LOGIN_PASSWORD required")
        self._assert_invalid_login(page, "   ", credentials["password"])

    def test_username_with_leading_trailing_spaces_cannot_login(self, page):
        if not credentials["username"] or not credentials["password"]:
            pytest.skip("LOGIN_USERNAME and LOGIN_PASSWORD required")
        self._assert_invalid_login(
            page, f"  {credentials['username']}  ", credentials["password"]
        )

    def test_sql_injection_attempt_cannot_login(self, page):
        self._assert_invalid_login(page, "' OR '1'='1", "' OR '1'='1")

    def test_special_characters_in_credentials_cannot_login(self, page):
        self._assert_invalid_login(page, "user@#$%", "pass!@#$%")

    def test_similar_but_wrong_password_missing_punctuation_cannot_login(self, page):
        if not credentials["username"]:
            pytest.skip("LOGIN_USERNAME required")
        self._assert_invalid_login(page, credentials["username"], "SimilarPassword")

    def test_similar_but_wrong_password_extra_character_cannot_login(self, page):
        if not credentials["username"] or not credentials["password"]:
            pytest.skip("LOGIN_USERNAME and LOGIN_PASSWORD required")
        self._assert_invalid_login(page, credentials["username"], credentials["password"] + "x")
