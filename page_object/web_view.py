from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from locator import XpathLocator
from .element import Element


class WebView:
    """Base representation of webview object."""

    def __init__(
        self,
        webdriver: WebDriver,
        wait_timeout: int,
        poll_frequency=float(0),
        **kwargs,
    ):
        """Set up webdriver and WebDriverWait."""
        self.webdriver: WebDriver = webdriver
        self.wait_timeout: int = wait_timeout
        self.wait = WebDriverWait(
            driver=webdriver,
            timeout=wait_timeout,
            poll_frequency=poll_frequency,
        )

    def init_element(self, locator: XpathLocator) -> Element:
        """Shortcut for initializing Element instances."""
        return Element(self, locator=locator)

    @property
    def current_url(self) -> str:
        return self.webdriver.current_url
