from selenium import webdriver
import time
import json

###############################################################################
#                               (Mobile)
#               This class is written to login to Trendsales
#                   and verify elements on landing page
#
###############################################################################


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    # Test the user login
    def user_login(self):

        with open("test_user.json") as data_file:
            data = json.load(data_file)

        # First accept cookies
        self.driver.find_element_by_xpath("//a[@data-qa-name='accept-cookies']").click()
        time.sleep(1)
        # Click the "Mit TS" button to enter the login screen    ---  Wanted method is commented out due to front-end variable not yet live
        #self.driver.find_element_by_xpath("//a[@data-qa-name='nav-account']").click()
        self.driver.get('https://m.trendsales.dk/account')
        time.sleep(1)
        # Send the login data & press the login buttons
        self.driver.find_element_by_xpath("//input[@data-qa-name='login-username']").send_keys(data["username"])
        self.driver.find_element_by_xpath("//input[@data-qa-name='login-password']").send_keys(data["password"])
        self.driver.find_element_by_xpath("//a[@data-qa-name='login-submit']").click()
        time.sleep(2)

        # Assert login was successful
        assert data["username"] in self.driver.find_element_by_xpath("//div[@data-qa-name='title']/div[contains(text(),'{}')]".format(data["username"])).text
        #print("User login is functional")

    # Function for verifying landing after login - check certain elements are present
    def landing(self):
        # This function should be run after login, however, the URL for this funtion is "m.trendsales.dk/account"
        assert "account" in self.driver.current_url
        try:
            self.driver.find_element_by_xpath("//div/a[@href='/account/conversations']")
            self.driver.find_element_by_xpath("//div/a[@href='/account/transactions']")
            self.driver.find_element_by_xpath("//div/a[@href='/account/listings/open']")
            self.driver.find_element_by_xpath("//div/a[@href='/account/trades/buyer']")
            self.driver.find_element_by_xpath("//div/a[@href='/account/likes']")
            self.driver.find_element_by_xpath("//div/a[@href='/account/profile']")
            #print("All elements are present upon landing")
        except:
            print("An element was not found in the landing page")
