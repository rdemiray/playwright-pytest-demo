class CarbonitePersonalTrialPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.carbonite.com/personal/trial/"
    
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
        return self.page.get_by_role("textbox", name="Country of residence*")

    def locator_for_country_of_residence_form_select_button(self):
        return self.page.get_by_role("button", name="form select button")
    
    def locator_for_country_in_the_form(self, country):
        return self.page.locator("li").filter(has_text=country)
    
    def locator_for_claim_button(self):
        return self.page.get_by_role("button", name="Claim Free Trial")
    
    def check_locator_for_email_communications_checkbox(self):
        self.page.get_by_role("checkbox", name="YES. I would like to receive").check()

    def click_i_am_not_a_robot_checkbox(self):
        self.page.locator("iframe[name=\"a-i8qo26dcv2is\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    
    def select_country_of_residence(self, country):
        self.locator_for_country_of_residence().click()
        self.locator_for_country_of_residence_form_select_button().click()
        self.locator_for_country_in_the_form(country).click()



    

    
    

    
