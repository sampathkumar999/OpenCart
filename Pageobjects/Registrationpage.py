from selenium import webdriver

class Registerpage:

    link_myaccount_xpath = "//span[normalize-space()='My Account']"
    link_register_xpath = "//a[normalize-space()='Register']"
    textbox_firstname_id = "input-firstname"
    textbox_lastname_id = "input-lastname"
    textbox_email_id = "input-email"
    textbox_telephone_id = "input-telephone"
    textbox_password_id = "input-password"
    textbox_confirmpassword_id = "input-confirm"
    radio_newslettersub_xpath = "//input[@value='1']"
    radio_newsletterunsub_xpath = "//input[@value='0']"
    privacypolicy_checkbox_xpath = "//input[@name='agree']"
    button_submit_xpath = "//input[@type='submit']"


    def __init__(self, driver):
        self.driver = driver


    def enterfirstname(self, firstname):
        self.driver.find_element_by_id(self.textbox_firstname_id).clear()
        self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(firstname)


    def enterlastname(self, lastname):
        self.driver.find_element_by_id(self.textbox_lastname_id).clear()
        self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(lastname)

    def enteremail(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def entertelephone(self, telephone):
        self.driver.find_element_by_id(self.textbox_telephone_id).clear()
        self.driver.find_element_by_id(self.textbox_telephone_id).send_keys(telephone)

    def enterpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def confirmpassword(self, confirmpassword):
        self.driver.find_element_by_id(self.textbox_confirmpassword_id).clear()
        self.driver.find_element_by_id(self.textbox_confirmpassword_id).send_keys(confirmpassword)

    def newssubscription(self):
        self.driver.find_element_by_xpath(self.radio_newsletterunsub_xpath).click()

    def tickprivacypolicy(self):
        self.driver.find_element_by_xpath(self.privacypolicy_checkbox_xpath).click()


    def clicksubmit(self):
        self.driver.find_element_by_xpath(self.button_submit_xpath).click()