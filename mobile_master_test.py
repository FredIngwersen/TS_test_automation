from selenium                               import webdriver
from selenium.webdriver.common.keys         import Keys
from selenium.webdriver.chrome.options      import Options
from user_login                             import Login
from search                                 import Search
import unittest
import sys
import time


# --------------------------------------------------------------------------#

# When using the unittest module every test function must start with "_test"
class Master_Test_TS_Mobile_Chrome(unittest.TestCase):

    # Anything declared in setUp will run for all test cases
    def setUp(self):
        # More information at: https://sites.google.com/a/chromium.org/chromedriver/mobile-emulation
        mobile_emulation = {"deviceName": "iPhone 6 Plus"}

        # A variable to hold the configurations
        chrome_options = webdriver.ChromeOptions()

        # Add the mobile emulation to the chrome options variable
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        # Create driver, pass in the chrome options
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    # Start the master test for iOS
    # This function is made up of tests written in seperate class files
    # First, it goes to the TS mobile site, then calls class functions
    def test_mobile_master(self):
        driver = self.driver

        # Goto trendsales mobile page
        driver.get('https://m.trendsales.dk/')

        # Login as a standard user
        Login(driver).user_login()

        # Secion for verifying elements
        Login(driver).landing()
        # Goto search
        #self.driver.find_element_by_xpath("//a[@data-qa-name='nav-search']").click()         #       <---  Waiting for qa variable name
        driver.get('https://m.trendsales.dk/')

        # This section goes through functionality of the search page
        Search(driver).listings()
        Search(driver).toggle()
        Search(driver).search_bar()
        #Search(driver).filters()                 #        <--- Not yet complete

    # Anything declared in tearDown will be executed for all test
    def tearDown(self):
        # Close the browser.
        # Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()
        self.driver.close()

# Boilerplate code to start the unit tests
if __name__ == "__main__":
	unittest.main()
