from collections.abc import Generator

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from .element import Element
from .locator import XPathLocator


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

    def init_element(self, locator: XPathLocator) -> Element:
        """Shortcut for initializing Element instances."""
        return Element(self, locator=locator)

    def init_elements(self, locator: XPathLocator) -> list[Element]:
        """Shortcut for initializing list of Element instances."""
        elements = []
        for loc in self.iter_locators(locator):
            elements.append(
                self.init_element(locator=loc)
            )
        return elements

    def iter_locators(self, locator: XPathLocator) -> Generator[XPathLocator, None, None]:
        """Get iterator over locators each of them match single element.

        For example, there are multiple elements on page that matches
        `XPathLocator("//a")`.
        This method return set of locators like
            * `XPathLocator("//a[1]")`
            * `XPathLocator("//a[2]")`
            ...

        """
        for index in range(1, len(self._get_elements(locator=locator)) + 1):
            yield locator + XPathLocator(f'[{index}]')

    def _get_element(self, locator: XPathLocator, only_visible=True) -> WebElement:
        """Get WebElement from page by using locator."""
        if only_visible:
            self.wait_until_visible(locator=locator)
        return self.webdriver.find_element(*locator)

    def _get_elements(self, locator: XPathLocator) -> list[WebElement]:
        """Get WebElements from page by using locator."""
        return self.webdriver.find_elements(*locator)

    def wait_until_clickable(self, locator: XPathLocator):
        """Wait until element matching locator becomes clickable."""
        try:
            self.wait.until(expected_conditions.element_to_be_clickable(locator))
        except TimeoutException:
            raise TimeoutException(
                f"{locator} is not clickable after {self.wait_timeout} seconds!",
            )

    def wait_until_visible(self, locator: XPathLocator):
        """Wait until element matching locator becomes visible."""
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(
                f"Unable to locate {locator} in {self.wait_timeout} seconds!",
            )

    def wait_until_invisible(self, locator: XPathLocator):
        """Wait until element matching locator becomes invisible."""
        try:
            self.wait.until(expected_conditions.invisibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(
                f"{locator} is still visible in {self.wait_timeout} seconds!",
            )

    @property
    def current_url(self) -> str:
        return self.webdriver.current_url
