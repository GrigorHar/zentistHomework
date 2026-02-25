from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/")

    def get_title(self):
        return self.page.title()

    def get_fork_me_on_github_link(self):
        return self.page.get_by_role("link", name="fork me on github")

    def get_content_links(self):
        return self.page.locator("#content a[href]")

    def get_links_count(self):
        return self.get_content_links().count()

    def click_form_authentication(self):
        self.page.get_by_role("link", name="Form Authentication").click()
