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

    # For verifying inbox contains elements
    def inbox(self):
        # URL : "m.trendsales.dk/account"
        self.driver.find_element_by_xpath("//a[@data-qa-name='nav-account']").click()
        try:
            self.driver.find_element_by_xpath("//div/a[@href='/account/conversations']").click()
            self.driver.find_element_by_xpath("//a[contains(@class, 'list__item')]")
            self.driver.find_element_by_xpath("//a[@data-qa-name='paneheader-back']").click()
        except:
            print("No messages were found in the inbox")

    # Check account has transactions and withdrawal accounts are present and can be added
    def wallet(self):
        # URL : "m.trendsales.dk/account"
        self.driver.find_element_by_xpath("//a[@data-qa-name='nav-account']").click()

        # Check account part
        self.driver.find_element_by_xpath("//div/a[@href='/account/transactions']").click()
        try:
            self.driver.find_element_by_xpath("//div[contains(@class, 'list__item')]")
        except:
            print("No transactions were found in the wallet")

        # Check withdrawal part
        try:
            self.driver.find_element_by_xpath("//a[@href='account/transactions/withdraw']").click()
            self.driver.find_element_by_xpath("//div[@data-qa-name='option']")
            self.driver.find_element_by_xpath("//a[@data-qa-name='edit-toggle']")
        except:
            print("No account or edit option elements found")

        try:
            self.driver.find_element_by_xpath("//a[@data-qa-name='edit-toggle']").click()
            self.driver.find_element_by_xpath("//div[@data-qa-name='add-option']").click()
            self.driver.find_element_by_xpath("//div[@data-qa-name='title' and contains(text(), 'Tilføj bankkonto')]")
            self.driver.find_element_by_xpath("//div[@data-qa-name='close']")
            self.driver.find_element_by_xpath("//a[@data-qa-name='paneheader-back']").click()
            # Click the back button - needs data-qa-name
        except:
            print("Edit or add bank account button is not functional")

    def  listings(self):
        # URL : "m.trendsales.dk/account"
        self.driver.get(config.getHostname() + "/account")

        self.driver.find_element_by_xpath("//div/a[@href='/account/listings/open']").click()

        # Retrieve number of open and closed listings

        ############### Needs data-qa-name to be finished #################


    def open_listings(self):
        print("")


    def favourites(self):
        print("")


    def profile(self):
        print("")
