from time import sleep
from browser import Browser
from selenium.webdriver.common.by import By

class ResultsPageElements(object):
    TITLE_TEXT = '/html/body/div[5]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/header/div/div[2]/div/div/div/div[1]/div/button[1]/div'

class ResultsPage(Browser):
    def get_title_text(self):
        sleep(2)
        return self.driver.find_element(By.XPATH, ResultsPageElements.TITLE_TEXT).text