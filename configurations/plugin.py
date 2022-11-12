import pytest
from _pytest.config import Config

from .selenium import SeleniumConfigurationPlugin


@pytest.hookimpl
def pytest_configure(config: Config):
    """Register uSummit plugins."""
    config.pluginmanager.register(
        plugin=SeleniumConfigurationPlugin(),
        name="selenium_configuration_plugin",
    )
