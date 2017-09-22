import json
import os

###############################################################################
#                             (Configuration)
#              This file is for centralizing variables such
#                      as usernames or hostnames etc.
#
###############################################################################


class Config(object):
    def __init__(self):
        with open("test_user.json") as data_file:
            self.data = json.load(data_file)


    def getUsername(self):
        return self.data["username"]
    def getPassword(self):
        return self.data["password"]

    def getHostname(self):
        return os.getenv('HOSTNAME', "https://m.trendsales.dk")

config = Config();
