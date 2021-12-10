from selenium import webdriver

class Loginpage:

    textbox_email_id = "input-email"
    textbox_password_id = "input-password"
    button_login_xpath = "//input[@value='Login']"


    def __init__(self, driver):
        self.driver = driver


    def enteremail(self, username):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(username)


    def enterpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)


    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()