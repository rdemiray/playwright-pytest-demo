from pages.base_page import BasePage
class CarbonitePersonalTrialPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page, url="https://www.carbonite.com/personal/trial/")
        

    ### Locators for elements on the Carbonite Personal Trial page ###
    
    def locator_for_signup_for_free_trial_heading(self):
        return self.page.get_by_role("heading", name="Sign-up for a FREE 15-day")

    def locator_for_email_address(self):
        return self.page.get_by_role("textbox", name="Email address*")
    
    def locator_for_confirm_email(self):
        return self.page.get_by_role("textbox", name="Confirm email*")
    
    def locator_for_password(self):
        return self.page.get_by_role("textbox", name="Password*", exact=True)
    
    def locator_for_confirm_password(self):
        return self.page.get_by_role("textbox", name="Confirm password*")
    
    def locator_for_country_of_residence(self):
        # return self.page.get_by_role("textbox", name="Country of residence*")
        return self.page.get_by_role("button", name="form select button")

    def locator_for_country_of_residence_form_select_button(self):
        return self.page.get_by_role("button", name="form select button")
    
    def locator_for_country_in_the_form(self, country):
        return self.page.locator("li").filter(has_text=country)
    
    def locator_for_claim_button(self):
        return self.page.get_by_role("button", name="Claim Free Trial")
    
    def locator_for_email_address_error(self):
        return self.page.get_by_text("The Email address field is required")
    
    def locator_for_confirm_email_error(self):
        return self.page.get_by_text("The Confirm email field is required")
    
    def locator_for_password_error(self):
        return self.page.get_by_text("The Password field is required")
    
    def locator_for_confirm_password_error(self):
        return self.page.get_by_text("The Confirm your password field is required")
    
    def locator_for_i_am_not_a_robot_checkbox_error(self):
        return self.page.get_by_text("This field is required*")
    
    ### Methods to interact with the Carbonite Personal Trial page ###
    
    def check_locator_for_email_communications_checkbox(self):
        self.page.get_by_role("checkbox", name="YES. I would like to receive").check()

    def click_i_am_not_a_robot_checkbox(self):
        self.page.locator("iframe[name=\"a-i8qo26dcv2is\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    
    def select_country_of_residence(self, country):
        self.locator_for_country_of_residence().click()
        self.locator_for_country_of_residence_form_select_button().click()
        self.locator_for_country_in_the_form(country).click()
    
  
