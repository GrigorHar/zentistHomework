import pytest
from playwright.sync_api import expect

from pages.main_page import MainPage


class TestScenario1MainPage:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.main_page = MainPage(page)
        self.main_page.goto()

    def test_open_main_page_assert_page_has_title(self):
        title = self.main_page.get_title()
        assert title
        assert len(title) > 0

    def test_assert_page_has_fork_me_on_github_element(self):
        fork_me_link = self.main_page.get_fork_me_on_github_link()
        expect(fork_me_link).to_be_attached()

    def test_assert_page_content_contains_44_links(self):
        links_count = self.main_page.get_links_count()
        assert links_count == 44
