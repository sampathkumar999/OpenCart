from selenium import webdriver

class Homepage:

    link_myaccount_xpath = "//span[normalize-space()='My Account']"
    link_customerRegistration_xpath = "//a[normalize-space()='Register']"
    link_customerLogin_xpath = "//a[normalize-space()='Login']"
    link_Wishlist_xpath = "//span[normalize-space()='Wish List (0)']"
    link_shoppingcart_xpath = "//span[normalize-space()='Shopping Cart']"
    searchbox_xpath = "//input[@placeholder='Search']"
    searchbutton_xpath = "//button[@class='btn btn-default btn-lg']"
    link_desktops_xpath = "//a[normalize-space()='Desktops']"
    link_desktopPCs_xpath = "//a[normalize-space()='PC (0)']"
    link_MACcomputers_xpath = "//a[normalize-space()='Mac (1)']"
    link_ALLcomputers_xpath = "//a[normalize-space()='Show All Desktops']"
    link_laptopsanddesktops_xpath = "//a[normalize-space()='Laptops & Notebooks']"
    link_MACs_xpath = "//a[normalize-space()='Macs (0)']"
    link_windows_xpath = "//a[normalize-space()='Windows (0)']"
    link_ALLLapsandWindows_xpath = "//a[normalize-space()='Show All Laptops & Notebooks']"
    link_components_xpath = "//a[normalize-space()='Components']"
    link_tablets_xpath = "//a[normalize-space()='Tablets']"
    link_software_xpath = "//a[normalize-space()='Software']"
    link_phonesandPDAs_xpath = "//a[normalize-space()='Phones & PDAs']"
    link_cameras_xpath = "//a[normalize-space()='Cameras']"
    link_MP3players_xpath = "//a[normalize-space()='MP3 Players']"
    link_checkout_xpath = "//span[normalize-space()='Checkout']"
    link_items_xpath = "//span[@id='cart-total']"



    def __init__(self, driver):
        self.driver = driver

    def Myaccountlink(self):
        self.driver.find_element_by_xpath(self.link_myaccount_xpath).click()

    def loginlink(self):
        self.driver.find_element_by_xpath(self.link_customerLogin_xpath).click()

    def Registrationlink(self):
        self.driver.find_element_by_xpath(self.link_customerRegistration_xpath).click()

    def wishlistlink(self):
        self.driver.find_element_by_xpath(self.link_Wishlist_xpath).click()

    def shoppingcartlink(self):
        self.driver.find_element_by_xpath(self.link_shoppingcart_xpath).click()

    def searchbox(self, product):
        self.driver.find_element_by_xpath(self.searchbox_xpath).send_keys(product)

    def clicksearch(self):
        self.driver.find_element_by_xpath(self.searchbutton_xpath).click()
