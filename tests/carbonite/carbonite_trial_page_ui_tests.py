from pages.carbonite_personal_trial_page import CarbonitePersonalTrialPage

def test_carbonite_ui_fields(page):
    carbonitePage = CarbonitePersonalTrialPage(page)
    carbonitePage.navigate_to_page()
    assert carbonitePage.locator_for_signup_for_free_trial_heading().is_visible(), "Sign-up for a FREE 15-day trial heading is not visible"
    assert carbonitePage.locator_for_email_address().is_visible(), "Email address field is not visible"
    assert carbonitePage.locator_for_confirm_email().is_visible(), "Confirm email field is not visible"
    assert carbonitePage.locator_for_password().is_visible(), "Password field is not visible"
    assert carbonitePage.locator_for_confirm_password().is_visible(), "Confirm password field is not visible"
    assert carbonitePage.locator_for_country_of_residence().is_visible(), "Country of residence field is not visible"
    assert carbonitePage.locator_for_claim_button().is_visible(), "Claim Free Trial button is not visible"

def test_carbonite_ui_field_validations(page):
    carbonitePage = CarbonitePersonalTrialPage(page)
    
    carbonitePage.locator_for_claim_button().click()

    assert carbonitePage.locator_for_email_address_error().is_visible(), "Email address error message is not visible"
    assert carbonitePage.locator_for_confirm_email_error().is_visible(), "Confirm email error message is not visible"
    assert carbonitePage.locator_for_password_error().is_visible(), "Password error message is not visible"
    assert carbonitePage.locator_for_confirm_password_error().is_visible(), "Confirm password error message is not visible"
    assert carbonitePage.locator_for_i_am_not_a_robot_checkbox_error().is_visible(), "I am not a robot checkbox error message is not visible"



    
    
    

# def test_carbonite_ui_field_validations(page):
    # carbonitePage = CarbonitePersonalTrialPage(page)
    # carbonitePage.navigate_to_page()
    
    # # Check for empty email field validation
    # carbonitePage.locator_for_email_address().fill("")
    # carbonitePage.locator_for_claim_button().click()
    # assert carbonitePage.locator_for_email_address_error().is_visible(), "Email address error message is not visible"

    # # Check for invalid email format validation
    # carbonitePage.locator_for_email_address().fill("invalid-email")
    # carbonitePage.locator_for_claim_button().click()
    # assert carbonitePage.locator_for_email_address_error().is_visible(), "Email address error message is not visible"

    # # Check for empty password field validation
    # carbonitePage.locator_for_password().fill("")
    # carbonitePage.locator_for_claim_button().click()
    # assert carbonitePage.locator_for_password_error().is_visible(), "Password error message is not visible"
    