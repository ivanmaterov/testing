from page_object.page import Page
from pages.components.navigation import Navigation
from pages.components.search_field import SearchField


class MainPage(Page):
    @property
    def search_field(self) -> SearchField:
        return SearchField(page=self)

    @property
    def navigation(self) -> Navigation:
        return Navigation(page=self)
