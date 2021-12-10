import pytest
from Pageobjects.Registrationpage import Registerpage
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen



class Test_001_registration:
    baseURL = Readconfig.getApplicationurl()
    logger = LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_registration(self, setup):

        self.logger.info("****************Test_001_Registration***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("****************starting customer registration***************")
        self.register = Registerpage(self.driver)
        self.driver.find_element_by_xpath(self.register.link_myaccount_xpath).click()
        self.driver.find_element_by_xpath(self.register.link_register_xpath).click()
        self.logger.info("************* Providing customer info **********")
        self.register.enterfirstname("sampath")
        self.register.enterlastname("kumar")
        self.register.enteremail("darlingsam1994@gmail.com")
        self.register.entertelephone("1234567890")
        self.register.enterpassword("samp666ath")
        self.register.confirmpassword("samp666ath")
        self.register.newssubscription()
        self.register.tickprivacypolicy()
        self.register.clicksubmit()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_xpath("//div[@id='content']/h1").text

        if "Your Account Has Been Created!" in self.msg:
            assert True
            self.logger.info("****************customer registration passed**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_RegCustomer_scr.png")
            self.logger.info("****************customer registration failed**************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending customer registration test **********")






