from playwright.sync_api import Page

from pages.login.password_input_page import PasswordInputPage

class SignInPage:
    """
    This class represents the sign-in page of the IceWarp mail client.
    """

    def __init__(self, page: Page):

        self.page = page
        self.username_input = page.locator("//input[@name = 'email-address']")
        self.continue_button = page.locator("//button[@name = 'next']")

    def navigate_to_login_page(self, url: str) -> None:
        """
        Goes to the login page.
        """

        self.page.goto(url)

    def fill_user_name(self, username: str) -> None:
        """
        Fills the username in the input.
        """

        self.username_input.fill(username)

    def click_continue_button(self) -> PasswordInputPage:
        """
        Clicks the continue button.
        """

        self.continue_button.click()

        return PasswordInputPage(self.page)