class BasePage:
    """
    Base class for all page objects.
    Contains common methods and properties that can be used by all pages.
    """

    def __init__(self, page, url=""):
        self.page = page
        self.url = url
        self.navigate_to_page()
        # Automatically accept cookies on page load
        self.accept_cookies()
    
    def locator_for_cookies_banner(self):
        """Locator for the cookies banner."""
        return self.page.get_by_label("Privacy", exact=True).locator("div").filter(has_text="We use cookies and similar").nth(1)
    
    def locator_for_accept_cookies_button(self):
        """Locator for the accept cookies button."""
        return self.page.get_by_role("button", name="Accept All")

    def navigate_to_page(self):
        """Navigate to the page URL."""
        self.page.goto(self.url)

    def accept_cookies(self, timeout=5000):
        """Accept cookies if the cookies banner becomes visible within timeout."""

        try:
            # Wait for the banner to appear, but only up to `timeout` ms
            self.locator_for_cookies_banner().wait_for(state="visible", timeout=timeout)
            self.locator_for_accept_cookies_button().click()
            print("Cookies accepted.")
        except:
            print("Cookies banner did not appear in time, no action taken.")