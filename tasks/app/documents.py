from playwright.sync_api import Page
from fragments.app.right_click_menu import RightClickMenuFragment

def create_document(page: Page) -> None:
    """
    Creates a document in the IceWarp browser app.
    """

    right_click_menu = RightClickMenuFragment(page)
    right_click_menu.create_new_document()