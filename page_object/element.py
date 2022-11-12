import os
import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from . import locator


class Element:
    """Base representation of element on page."""

    def __init__(self, web_view, locator: locator.XPathLocator):
        """Init page element."""
        self.web_view = web_view
        self.locator: locator.Locator = locator

    def wait_until_visible(self):
        self.web_view.wait_until_visible(locator=self.locator)

    def wait_until_invisible(self):
        self.web_view.wait_until_invisible(locator=self.locator)

    def wait_until_clickable(self):
        self.web_view.wait_until_clickable(locator=self.locator)

    def wait_until_text_is_in_element(self, text: str):
        self.web_view.wait_until_text_is_in_element(text=text, locator=self.locator)

    @property
    def exists_in_dom(self) -> bool:
        return len(self.web_view._get_elements(locator=self.locator)) != 0

    @property
    def is_displayed(self) -> bool:
        return self.get_element(only_visible=False).is_displayed()

    def fill(
        self,
        text: str,
        only_visible=True,
        clear=True,
    ):
        """Fill element with text."""
        if clear:
            self.clear(only_visible=only_visible)
        input_text = str(text)
        self.send_keys(input_text, only_visible=only_visible)

    def clear(self, only_visible=True):
        """Clear input and it's value."""
        self.get_element(only_visible=only_visible)

        try:
            self.send_keys(Keys.CONTROL + "a")
            self.send_keys(Keys.DELETE)
        except Exception:
            while self.get_value() != "":
                self.send_keys(Keys.BACK_SPACE)

    def click(self, only_visible=True, wait_until_clickable=True, sleep_time: float = 0.0):
        """Click on element."""
        time.sleep(sleep_time)
        # Try except block help to overcome error `Element is not attached to page` error.
        attempts = 0
        max_attempts = int(os.environ.get("MAX_RETRY_ATTEMPTS", 3))
        while True:
            try:
                attempts += 1
                if wait_until_clickable:
                    self.wait_until_clickable()
                self.get_element(only_visible=only_visible).click()
                break
            except StaleElementReferenceException:
                if attempts >= max_attempts:
                    raise StaleElementReferenceException

    def get_text(self, only_visible=True) -> str:
        """Get text from element."""
        return self.get_element(only_visible=only_visible).text

    def get_attribute(self, attribute_name: str, only_visible=True) -> str:
        """Get value of attr from element."""
        return self.get_element(only_visible=only_visible).get_attribute(name=attribute_name)

    def get_element(self, only_visible=True) -> WebElement:
        """Get selenium instance(WebElement) of element."""
        return self.web_view._get_element(locator=self.locator, only_visible=only_visible)

    def send_keys(self, keys: str, only_visible=True):
        self.get_element(only_visible=only_visible).send_keys(*keys)

    def get_value(self, only_visible=True):
        """Get value of value attr from element."""
        return self.get_attribute(attribute_name="value", only_visible=only_visible)
