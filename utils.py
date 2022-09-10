from lib2to3.pgen2 import driver
from browser import Browser

class Utils(Browser):

    def navigate(self, url):
        self.driver.get(url)