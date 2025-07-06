from pages.carbonite_personal_trial_page import CarbonitePersonalTrialPage
import pytest
from data.test_data import test_data_for_tc3

@pytest.mark.tc3
def test_carbonite_trial_page_happy_path(page, expect):
    carbonitePage = CarbonitePersonalTrialPage(page)
    carbonitePage.navigate_to_page()

    # Fill in the form fields
    carbonitePage.locator_for_email_address().fill(test_data_for_tc3.email)
    carbonitePage.locator_for_confirm_email().fill(test_data_for_tc3.email)
    carbonitePage.locator_for_password().fill(test_data_for_tc3.password)
    carbonitePage.locator_for_confirm_password().fill(test_data_for_tc3.password)
    carbonitePage.select_country_of_residence(test_data_for_tc3.country)
    carbonitePage.check_locator_for_email_communications_checkbox()
    carbonitePage.click_i_am_not_a_robot_checkbox()
    
    """Download does not work for some reason in automated Chromium browser. """
    #download_and_installation_page = None
    # with page.expect_download(timeout=30000) as download_info:
    #     download_and_installation_page = carbonitePage.click_claim_button()
    # download = download_info.value

    download_and_installation_page = carbonitePage.click_claim_button()
    expect(download_and_installation_page.page).to_have_url(download_and_installation_page.url)
    expect(download_and_installation_page.locator_welcome_to_carbonite_heading()).to_be_visible()
    expect(download_and_installation_page.locator_for_installation_steps()).to_be_visible()
    