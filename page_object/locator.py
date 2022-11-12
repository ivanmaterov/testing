from selenium.webdriver.common.by import By


class XPathLocator:
    """Base locator for looking for elements in page."""

    def __init__(self, query: str):
        """Init locator."""
        self.by: By = By.XPATH
        self.query: str = query

    def __iter__(self):
        """Unpack locator"""
        return iter((self.by, self.query))

    def __repr__(self):
        return f"Locator<By `{self.by}`: Query `{self.query}`>"

    def __add__(self, other: "XPathLocator"):
        """Provide ability to implement nested XPath locators"""
        return XPathLocator(query=self.query + other.query)
