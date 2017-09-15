from selenium import webdriver
import time

class Verify(object):

    def __init__(self, driver):
        self.driver = driver

    # Function for verifying landing
    def landing(self):
        assert "account" in self.driver.current_url
        try:
            self.driver.find_element_by_xpath("//div/a[@href='/account/conversations']")
            self.driver.find_element_by_xpath("//div/a[@href='/account/transactions']")
            self.driver.find_element_by_xpath("//div/a[@href='/account/open']")
            self.driver.find_element_by_xpath("//div/a[@href='/account/buyer']")
            self.driver.find_element_by_xpath("//div/a[@href='/account/likes']")
            self.driver.find_element_by_xpath("//div/a[@href='/account/profile']")

            print("All elements are present upon landing")
        except ElementNotFoundError:
            print("An element was not found in the landing page")


    # Function for verifying filters
    def filters(self):
        print("")

    # Function for verifying inbox
    def inbox(self):
        print("")
