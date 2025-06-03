import pytest
from selene import browser

@pytest.fixture()
def open_browser_with_size():
    browser.open('https://duckduckgo.com/')
    browser.config.window_width = 1200
    browser.config.window_height = 1024
    yield
    browser.quit()
