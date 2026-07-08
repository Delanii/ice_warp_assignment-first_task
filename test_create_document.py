from playwright.sync_api import Page

from fragments.app.app_header import AppHeaderFragment
from tasks.login.login import login_platform

def test_create_document(setup_browser_instance: Page,
                         get_login_credentials: dict) -> None:
    """
    """

    app_header = AppHeaderFragment(setup_browser_instance, get_login_credentials["username"])

    dashboard_page = login_platform(setup_browser_instance,
                                    get_login_credentials,
                                    app_header)

    dashboard_page.center_area.click(button = "right")
    
    general_menu = dashboard_page.page.locator("//ul[@role = 'menu']")
    general_menu.wait_for(state = "visible", timeout = 1_000)

    new_item_option = general_menu.locator("//li[@data-key = 'new']")
    new_item_option.hover()

    new_document_option = general_menu.locator("//li[@data-key = 'document']")
    new_document_option.wait_for(state = "visible", timeout = 1_000)
    new_document_option.click()