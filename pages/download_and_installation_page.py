from pages.base_page import BasePage

class DownloadAndInstallationPage(BasePage):
    """
    Page object for the Download and Installation page.
    Contains locators and methods specific to this page.
    """

    def __init__(self, page):
        super().__init__(page, url="https://www.carbonite.com/install/download/")
        # URL = https://www.carbonite.com/install/download/?packageid=4486&Action=INSTALL&RegistrationGUID=c054d66a-7bf6-4ee7-a3f8-5f202976cf0d&uid=9831699&activationcode=TRIAL-04486-107D53BC-1AEE-4123-9C25-49CBD3BA9C68&__upAuth=BBD45F081FCD3EB1CFA707C2D9DCC02C8D1F134EC8CEBD3913DDAF8A700BC139C146A3910678CF1AA436D8D6C75DC1FF204B3B52D5491CA57E972BD96B897029F2ADC9BCF267A0D6EE92AE3F7B4B3B6030BEB5A4900B7DF1EEE27E3EE79BB0F7D358C9F9EC0072546F5D49ECFAF518B93E7D7593B075A7CE2AA15A72AF84C21F30CA31C6A44D3CF78145A68072311BA1C01DFBDF3B89DE8F4F608457ED55EC8AF8161A3D96C0F169B524E9C2F4429148726BDD47AA477685F2C6D87A128B8E92339C52EDC4505DC45ACD7EBBEAEF85D3A3D746CC

    ### Locators for elements on the Download and Installation page ###

    def locator_welcome_to_carbonite_heading(self):
        return self.page.get_by_role("heading", name="Welcome to Carbonite Safe!")
    
    def locator_for_download_button(self):
        return self.page.get_by_role("link", name="Download")
    
    def locator_for_installation_steps(self):
        return self.page.get_by_text("Follow these steps to install Carbonite Safe.1. Download the Installer File")
    

    
