from selenium       import webdriver
from config         import config
import time


###############################################################################
#                               (Mobile)
#               This class is written to test functionality and
#                   verify elements on the account page
#
###############################################################################


class MyTS(object):

    def __init__(self, driver):
        self.driver = driver

    # Function for verifying inbox
    def inbox(self):
        # URL : "m.trendsales.dk/account/conversations"
        self.driver.get(config.getHostname() + "/account")
        self.driver.find_element_by_xpath("//div/a[@href='/account/conversations']").click()
        try:
            self.driver.find_element_by_xpath("//a[contains(@class, 'list__item')]")
        except:
            print("No messages were found in the inbox")

    def wallet(self):
        # URL : "m.trendsales.dk/account/conversations"
        self.driver.get(config.getHostname() + "/account")
        self.driver.find_element_by_xpath("//div/a[@href='/account/conversations']").click()
        try:
            self.driver.find_element_by_xpath("//div[contains(@class, 'list__item')]")
        except:
            print("No transactions were found in the inbox")

        self.driver.find_element_by_xpath("//a[@href='account/transactions/withdraw']").click()

    def  listings(self):
        print("")


    def open_listings(self):
        print("")


    def favourites(self):
        print("")


    def profile(self):
        print("")
