from playwright.sync_api import Page

from forms.edit_document import EditDocumentForm
from fragments.app.right_click_menu import RightClickMenuFragment

def create_document(page: Page,
                    document_name: str) -> EditDocumentForm:
    """
    Creates a document in the IceWarp browser app.
    """

    right_click_menu = RightClickMenuFragment(page)

    create_document_form = right_click_menu.create_new_document()
    create_document_form.fill_document_name(document_name)
    create_document_form.click_ok_button()

    return EditDocumentForm(page)