from playwright.sync_api import Page

from fragments.app.app_header import AppHeaderFragment

class DashboardPage:
    """
    The dashboard page of the IceWarp app.

    When instantiating the page, it waits for the dashboard menu to be visible, ensuring that the page has loaded.
    """

    def __init__(self, page: Page,
                username: str):

        self.page = page
        self.app_header = AppHeaderFragment(page, username)
        self.dashboard_menu = page.locator("//a[@class = 'd dashboard']")
        self.center_area = page.locator("//div[@data-iw-test = 'desktop.grid']")

        try:
            self.page.locator(self.app_header.avatar_button_locator).wait_for(state = "visible", timeout = 120_000)
        except TimeoutError:
            raise Exception("Dashboard page did not load within the expected time.")