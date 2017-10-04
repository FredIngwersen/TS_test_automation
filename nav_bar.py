from selenium       import webdriver
from config         import config
import time


###############################################################################
#                               (Mobile)
#               This class is written to test functionality and
#                   verify elements on the navigation bar
#
###############################################################################


class NavBar(object):

    def __init__(self, driver):
        self.driver = driver
