from time import sleep
from browser import Browser
from selenium.webdriver.common.by import By

class HeaderPageElements(object):
    WHERE_BTN = 'button'
    INPUT_SEARCH = 'bigsearch-query-location-input'
    SEARCH_BTN = '//*[@id="search-tabpanel"]/div/div[5]/div[1]/div[2]/button'

class HeaderPage(Browser):
    def where_btn(self):
        sleep(2)
        self.driver.find_element(By.TAG_NAME, HeaderPageElements.WHERE_BTN).click()

    def input_search(self, text):
        sleep(2)
        self.driver.find_element(By.ID, HeaderPageElements.INPUT_SEARCH).send_keys(text)

    def search_btn(self):
        sleep(2)
        self.driver.find_element(By.XPATH, HeaderPageElements.SEARCH_BTN).click()
