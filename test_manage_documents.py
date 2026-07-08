from playwright.sync_api import Page

from tasks.login.login import login_platform
from tasks.app.documents import create_document

def test_manage_documents(setup_browser_instance: Page,
                         get_login_credentials: dict) -> None:
    """
    """

    dashboard_page = login_platform(setup_browser_instance,
                                    get_login_credentials)

    dashboard_page.center_area.click(button = "right")
    create_document(dashboard_page.page) 