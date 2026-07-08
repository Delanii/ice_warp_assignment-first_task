from playwright.sync_api import Page

from forms.confirm_delete import ConfirmDeleteForm

class DocumentContextMenuFragment:
    """
    Fragment representing the context menu when right-clicking a document.
    """

    def __init__(self, page: Page):
        self.page = page
        self.menu_locator = page.locator("//ul[@role = 'menu']")
        self.delete_option_locator = self.menu_locator.locator("//li[@role = 'menuitem' and @data-key = 'DELETE']")

    def click_delete(self) -> ConfirmDeleteForm:
        """
        Clicks the delete option in the document context menu.
        """

        self.delete_option_locator.click()

        return ConfirmDeleteForm(self.page)