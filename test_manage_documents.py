from playwright.sync_api import Page, expect

from tasks.login.login import login_platform
from tasks.app.documents import create_document

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

    assert dashboard_page.verify_document_exists(document_name) == True