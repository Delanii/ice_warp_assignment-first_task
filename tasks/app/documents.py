from playwright.sync_api import Page, Locator

from forms.edit_document import EditDocumentForm
from fragments.app.document_context_menu import DocumentContextMenuFragment
from fragments.app.right_click_menu import RightClickMenuFragment

from pages.app.dashboard_page import DashboardPage

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

def verify_document_exists(dashboard_page: DashboardPage,
                        document_name: str) -> bool:
    """
    Verifies if a document with the specified name exists in the dashboard.
    """

    try:
        dashboard_page.center_area.get_by_text(document_name).wait_for(state = "visible", timeout = 2_000)
        return True
    except TimeoutError:
        return False

def find_document(dashboard_page: DashboardPage,
                  document_name: str) -> Locator:
    """
    Finds and returns the locator for a document with the specified name in the dashboard.
    """

    return dashboard_page.center_area.get_by_text(document_name)

def delete_document(document_context_menu: DocumentContextMenuFragment) -> None:
    """
    Deletes a document.
    """

    confirm_dialog = document_context_menu.click_delete()

    confirm_dialog.confirm_delete()