from playwright.sync_api import Page

class PasswordInputPage:
    """
    This class represents the password input page of the IceWarp mail client.
    """

    def __init__(self, page: Page):

        self.page = page
        self.password_input = page.locator("//input[@name = 'password']")
        self.sign_in_button = page.locator("//button[@name = 'next']")

    def fill_password(self, password: str) -> None:
        """
        Fills the password in the input.
        """

        self.password_input.fill(password)

    def click_sign_in_button(self) -> None:
        """
        Clicks the sign-in button.
        """

        self.sign_in_button.click()