import unittest
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from user_login import Login

# --------------------------------------------------------------------------#

# When using the unittest module every test function must start with "_test"
class Login_TS_iOS_Chrome(unittest.TestCase):

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

    # Test the user login
    def test_user_login(self):
        driver = self.driver

        # Goto trendsales mobile page
        driver.get('https://m.trendsales.dk/')

        # Use the Login class to login
        login = Login(driver)
        login.user_login()


    # Anything declared in tearDown will be executed for all test
    def tearDown(self):
        # Close the browser.
        # Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()
        self.driver.close()

# Boilerplate code to start the unit tests
if __name__ == "__main__":
	unittest.main()
