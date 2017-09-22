from selenium import webdriver
import time


###############################################################################
#                               (Mobile)
#               This class is written to test functionality and
#               verify elements on the Trendsales search page
#
###############################################################################


class Search(object):

    def __init__(self, driver):
        self.driver = driver

    # Check listings are present in search
    def listings(self):
        # URL : "m.trendsales.dk"
        try:
            self.driver.find_element_by_xpath("//a[@data-qa-name='listing-item']")
            #print("Listings are present")
        except:
            print("Listings were not found")

    # Check the toggle elements are present and functional
    def toggle(self):
        # URL : "m.trendsales.dk"
        try:
            self.driver.find_element_by_xpath("//div[@data-qa-name='view-mode']")
            self.driver.find_element_by_xpath("//a[@data-qa-name='listing-item' and contains(@class, 'listitem__listingItem')]")
            # Click to toggle view modes and check the tiles change
            self.driver.find_element_by_xpath("//div[@data-qa-name='view-mode']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//a[@data-qa-name='listing-item' and contains(@class, 'listitem__full')]")
            # Click again to toggle view mode and check tiles change
            self.driver.find_element_by_xpath("//div[@data-qa-name='view-mode']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//a[@data-qa-name='listing-item' and contains(@class, 'listitem__threeCol')]")
            #print("View mode toggling works as expected")
        except:
            print("View mode toggling has errors")

    # Check search bar present and functional
    def search_bar(self):
        # URL : "m.trendsales.dk"
        try:
            self.driver.find_element_by_xpath("//input[@data-qa-name='tagbar-input']")
            self.driver.find_element_by_xpath("//input[@data-qa-name='tagbar-input']").send_keys("jakker")
            self.driver.find_element_by_xpath("//a[@data-qa-name='tagbar-button']").click()
            time.sleep(1)
            self.driver.find_elements_by_xpath("//a[@data-qa-name='listing-item']")
            #print("Search bar is present and functional")
        except:
            print("Search bar is either not present or functional")

    # Function for verifying filters
    def filters(self):
        # URL : "m.trendsales.dk/filter"
        print("")
