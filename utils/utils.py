from playwright.sync_api import Page

def get_viewport_size(page: Page) -> dict:
    """
    Returns the viewport size for the browser context.
    """

    return {
        "width": page.evaluate("window.innerWidth"),
        "height": page.evaluate("window.innerHeight")
    }