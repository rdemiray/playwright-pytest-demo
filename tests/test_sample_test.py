# from pages.carbonite_personal_trial_page import CarbonitePersonalTrialPage




# def test_login(page):
#     page.goto("https://example.com/login")
#     login = LoginPage(page)
#     login.login("myuser", "mypassword")
#     assert page.url == "https://example.com/dashboard"



# import re
# from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
#     """
#     Tests if the Playwright website's title contains the expected substring.
#     """
#     page.goto("https://playwright.dev/")
#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(page: Page):
#     """
#     Tests clicking the "Get started" link and verifying the heading on the next page.
#     """
#     page.goto("https://playwright.dev/")
#     # Click the "Get started" link.
#     page.get_by_role("link", name="Get started").click()
#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()



import re
from playwright.sync_api import expect

def test_has_title(page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()