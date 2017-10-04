from selenium import webdriver
import time


###############################################################################
#                               (Mobile)
#               This class is written to test functionality and
#               verify elements on the Trendsales activity page
#
###############################################################################


class Activity(object):

    def __init__(self, driver):
        self.driver = driver
