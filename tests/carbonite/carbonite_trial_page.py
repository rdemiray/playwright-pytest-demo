from pages.carbonite_personal_trial_page import CarbonitePersonalTrialPage

def test_carbonite(page):
    carbonitePage = CarbonitePersonalTrialPage(page)
    carbonitePage.navigate_to_page()
    assert carbonitePage.locator_for_signup_for_free_trial_heading().is_visible(), "Sign-up for a FREE 15-day trial heading is not visible"
    assert carbonitePage.locator_for_email_address().is_visible(), "Email address field is not visible"
    assert carbonitePage.locator_for_confirm_email().is_visible(), "Confirm email field is not visible"
    assert carbonitePage.locator_for_password().is_visible(), "Password field is not visible"
    assert carbonitePage.locator_for_confirm_password().is_visible(), "Confirm password field is not visible"
    assert carbonitePage.locator_for_country_of_residence().is_visible(), "Country of residence field is not visible"
    assert carbonitePage.locator_for_claim_button().is_visible(), "Claim Free Trial button is not visible"
    