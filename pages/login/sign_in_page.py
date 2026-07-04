from playwright.sync_api import Page

class SignInPage:
    """

    """

    def __init__(self, page: Page):

        self.page = page
        self.username_input = page.locator("//input[@name = 'email-address']")
        self.continue_button = page.locator("//button[@name = 'next']")

    def navigate_to_login_page(self, url: str) -> None:
        """
        """

        self.page.goto(url)

    def fill_user_name(self, username: str) -> None:
        """
        """

        self.username_input.fill(username)

    def click_continue_button(self) -> None:
        """
        """

        self.continue_button.click()