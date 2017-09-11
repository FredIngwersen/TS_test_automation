from selenium import webdriver
import time
import json

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
        # Click the "Mit TS" button to enter the login screen
        self.driver.find_element_by_xpath("//a[@data-reactid='444']").click()
        time.sleep(1)
        # Send the login data & press the login buttons
        self.driver.find_element_by_xpath("//input[@data-qa-name='login-username']").send_keys(data["username"])
        self.driver.find_element_by_xpath("//input[@data-qa-name='login-password']").send_keys(data["password"])
        self.driver.find_element_by_xpath("//a[@data-qa-name='login-submit']").click()
        time.sleep(2)
