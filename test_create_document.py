from playwright.sync_api import Page

from tasks.login.login import login_platform

def test_create_document(setup_browser_instance: Page,
                         get_login_credentials: dict) -> None:
    """
    """

    dahsboard_page = login_platform(setup_browser_instance, get_login_credentials)