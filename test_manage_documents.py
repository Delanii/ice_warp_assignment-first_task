from playwright.sync_api import Page, expect

from tasks.login.login import login_platform
from tasks.app.documents import create_document, verify_document_exists, find_document

from utils.utils import create_unique_string

def test_manage_documents(setup_browser_instance: Page,
                         get_login_credentials: dict) -> None:
    """
    """

    dashboard_page = login_platform(setup_browser_instance,
                                    get_login_credentials)

    dashboard_page.center_area.click(button = "right")

    document_name = "automat_" + create_unique_string()
    edit_document_form = create_document(dashboard_page.page, document_name)
    edit_document_form.close_edit_document_form()

    assert verify_document_exists(dashboard_page, document_name) is True

    document_locator = find_document(dashboard_page, document_name)

    document_locator.click(button = "right")
    document_context_menu = dashboard_page.page.locator("//ul[@role = 'menu']")
    document_context_menu.locator("//li[@role = 'menuitem' and @data-key = 'DELETE']").click()

    confirm_dialog = dashboard_page.page.locator("dialog[open]")
    confirm_dialog.locator("footer button").first.click()