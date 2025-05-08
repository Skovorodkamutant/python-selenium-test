import time
from argparse import Action

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base


class Main_page(Base):
    #Класс для главной страницы

    url = 'https://www.wildberries.ru/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    #Locators
    search_field = "//input[@id='searchInput']"
    header_page = "//h1[@class='searching-results__title']"



    #Getters
    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_header_page(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.header_page)))

    #Actions
    def input_search_field(self):
        self.get_search_field().send_keys("электроника")
        print("Значение введено в поле")

    def press_enter_search_field(self):
        self.get_search_field().send_keys(Keys.RETURN)
        print("Нажали Enter")




    #Methods

    def search_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(2)
        self.input_search_field()
        self.press_enter_search_field()
        self.assert_word(self.get_header_page(), "электроника")

