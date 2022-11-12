from functools import cached_property

from page_object.component import Component
from page_object.element import Element
from page_object.locator import XPathLocator


class Navigation(Component):
    """Navigation bar component.

    Represents navigation bar that allows to toggle between main pages on the
    site.

    """
    @cached_property
    def navigation_element(self) -> Element:
        return self.init_element(
            locator=XPathLocator(
                query='//div[contains(@class, "content-menu")]/ul[@class="list"]',
            ),
        )

    def get_navigation_links(self) -> list[Element]:
        """Get navigation links from main page.

        It looks like navigation buttons below search field.

        """
        navigation_locator = self.navigation_element.locator
        return self.init_elements(
            locator=navigation_locator + XPathLocator('/li')
        )

    def wait_until_navigation_display_page(self, page_name: str):
        """Wait until navigation displays the name of page."""
        # hack to avoid cases when the first letter
        # on the page is capital. Selenium can't use
        # XPath2 and I don't know a solution how to write
        # case insensitive XPath search by text here
        text = page_name[1:]
        self.init_element(
            locator=XPathLocator(
                #
                query=f'//div[@id="navigation"]//*[contains(text(), "{text}")]'
            ),
        ).wait_until_visible()
