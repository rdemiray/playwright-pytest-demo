import pytest
from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import expect as playwright_expect



@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.set_default_timeout(15000)  # Set to 15 seconds
    yield page
    context.close()

@pytest.fixture
def expect():
    return playwright_expect