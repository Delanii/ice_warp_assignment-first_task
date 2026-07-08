from playwright.sync_api import Page

class CreateDocumentForm:
    """
    Represents the form for creating a document in the IceWarp web application.
    """

    def __init__(self, page: Page):
        self.page = page

        self.form_locator = page.locator("//div[@id = 'gui.gw']")
        self.form_locator.wait_for(state = "visible", timeout = 1_000)

        self.name_input_locator = self.form_locator.locator("//input[@class = 'full_width name']")
        self.ok_button_locator = self.form_locator.locator("//input[@id = 'gui.gw.x_btn_ok#main']")

    def fill_document_name(self, document_name: str) -> None:
        """
        Fills in the document name. The name is entered character by character to simulate user input.
        """

        self.name_input_locator.click()
        self.name_input_locator.press_sequentially(document_name)

    def click_ok_button(self) -> None:
        """
        Clicks the OK button to submit the form.
        """

        self.ok_button_locator.click()