class EditDocumentForm:
    """
    Represents the edit document form in the IceWarp web application.
    """

    def __init__(self, page):
        self.page = page

        self.form_locator = page.locator("//div[@id = 'gui.doc']")
        self.form_locator.wait_for(state = "visible", timeout = 1_000)

        editor_iframe_locator = self.form_locator.frame_locator("//iframe[@name = 'frameEditor']")

        self.typing_area_locator = editor_iframe_locator.locator("//div[@id = 'id_main_view']")
        self.typing_area_locator.wait_for(state = "visible", timeout = 120_000)

        self.close_locator = self.form_locator.locator("//div[@id = 'gui.doc#rem']")

    def close_edit_document_form(self) -> None:
        """
        Closes the edit document form.
        """

        self.close_locator.click()