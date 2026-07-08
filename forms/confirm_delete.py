from playwright.sync_api import Page

class ConfirmDeleteForm:
    """
    Represents the confirm delete form in the application.
    """

    def __init__(self, page: Page):
        self.page = page
        self.dialog = page.locator("dialog[open]")

    def confirm_delete(self) -> None:
        """
        Confirms the deletion of the object (document).
        """

        self.dialog.locator("footer button").first.click()