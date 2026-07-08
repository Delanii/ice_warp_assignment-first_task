from playwright.sync_api import Page

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
    create_document(dashboard_page.page)

    new_document_form = dashboard_page.page.locator("//div[@id = 'gui.gw']")
    new_document_form.wait_for(state = "visible", timeout = 1_000)

    new_document_name = "automat_" + create_unique_string()
    new_document_form.locator("//input[@class = 'full_width name']").click()
    new_document_form.locator("//input[@class = 'full_width name']").press_sequentially(new_document_name)
    new_document_form.locator("//input[@id = 'gui.gw.x_btn_ok#main']").click()