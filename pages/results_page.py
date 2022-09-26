from lib2to3.pgen2 import driver
from time import sleep
from browser import Browser
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd

class ResultsPageElements(object):
    TITLE_TEXT = '/html/body/div[5]/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/header/div/div[2]/div/div/div/div[1]/div/button[1]/div'

class ResultsPage(Browser):
    def get_title_text(self):
        sleep(2)
        return self.driver.find_element(By.XPATH, ResultsPageElements.TITLE_TEXT).text

    def get_accommodations_info(self):
        sleep(3)
        page_content = self.driver.page_source 
        site = BeautifulSoup(page_content, 'html.parser')  

        property_list = []

        properties = site.findAll('div', attrs={'itemprop': 'itemListElement'})

        for _property in properties:
            
            prop_url = _property.find('meta', attrs={'itemprop': 'url'})
            prop_url = prop_url['content']

            prop_name = _property.find('div', attrs={'class': 't1jojoys dir dir-ltr'})

            prop_desc = _property.find('meta', attrs={'itemprop': 'name'})
            prop_desc = prop_desc['content']

            night_prop_price = _property.find('span', attrs={'class': '_tyxjp1'})

            property_list.append([prop_url, prop_name.text, prop_desc, night_prop_price.text])


