from playwright.sync_api import Page

from forms.create_document import CreateDocumentForm

class RightClickMenuFragment:
    """
    Represents the right-click context menu in the IceWarp browser app.
    """

    def __init__(self, page: Page):

        self.page = page
        self.menu_frame = page.locator("//ul[@role = 'menu']")

        self.menu_frame.wait_for(state = "visible", timeout = 1_000)

        self.new_item_option = self.menu_frame.locator("//li[@data-key = 'new']")
        self.new_document_option = self.menu_frame.locator("//li[@data-key = 'document']")

    def create_new_document(self) -> CreateDocumentForm:
        """
        Navigates to create a new document in the right-click context menu.
        """

        self.new_item_option.hover()
        self.new_document_option.wait_for(state = "visible", timeout = 1_000)
        self.new_document_option.click()

        return CreateDocumentForm(self.page)