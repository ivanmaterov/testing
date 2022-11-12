import os

from selenium.webdriver.remote.webdriver import WebDriver

from page_object.web_view import WebView


class Page(WebView):
    """Base representation of page.

    It contains element and components of page and utils methods for page
    manipulation.

    """
    def __init__(
        self,
        webdriver: WebDriver,
        wait_timeout=int(os.environ.get("BROWSER_WAIT")),
        poll_frequency=float(os.environ.get("BROWSER_POLL_FREQUENCY")),
        **kwargs,
    ):
        super().__init__(webdriver, wait_timeout, poll_frequency, **kwargs)
