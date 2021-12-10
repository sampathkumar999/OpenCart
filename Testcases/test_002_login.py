import pytest
from selenium import webdriver
from Pageobjects.Loginpage import Loginpage
from Pageobjects.Homepage import Homepage
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen


class Test_loginpage:

    base_url = Readconfig.getApplicationurl()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.hp = Homepage(self.driver)
        self.lp = Loginpage(self.driver)
        self.hp.Myaccountlink()
        self.hp.loginlink()
        self.lp.enteremail(self.username)
        self.lp.enterpassword(self.password)
        self.lp.clicklogin()
        logintitle = self.driver.title
        if logintitle == "My Account":
            assert True
            self.logger.info('****************logintest passed******************')
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots" + "test_login.png")
            self.driver.close()
            self.logger.error('****************logintest failed******************')
            assert False
