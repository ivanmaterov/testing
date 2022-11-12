from .web_view import WebView


class Component(WebView):
    """Base representation of page component.

    It contains elements of page and utils methods for page
    manipulation, but as separate entity that can be reused for different pages
    with common elements.

    """

    def __init__(self, page):
        super().__init__(
            webdriver=page.webdriver,
            wait_timeout=page.wait_timeout,
        )
        self.page = page
