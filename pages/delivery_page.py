import time
from argparse import Action

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base


class Delivery_page(Base):
    #Класс для страницы выбора пункта доставки



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    #Locators
    field_address = "//input[@class='map-search__input']"
    search_address_button = "(//span[@class='map-search__suggest-title'])[1]"
    address_icon = "//img[@class='icon-img']"
    address = "//span[@class='address-item__name-text']/span[text()='Усть-Каменогорск, улица Ломоносова 43/2']"
    confirm_address = "//button[@class='details-self__btn btn-main']"
    map = "//div[@class='geo-block__map maplibregl-map']"





    #Getters
    def get_delivery_address(self):
        return WebDriverWait(self.driver, 90).until(
            EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_field_address(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.field_address)))


    def get_search_address_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.search_address_button)))


    def get_address_icon(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.address_icon)))

    def get_confirm_address(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_address)))


    def get_map(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.map)))


    #Actions
    def visible_map(self):
        self.get_map().is_displayed()
        print("дожидаемся отображения карты")


    def input_field_address(self):
        self.get_field_address().send_keys("Усть-Каменогорск, улица Ломоносова 43/2")
        print("Ввод конкретного адреса пункта выдачи")

    def click_search_address_button(self):
        self.get_search_address_button().click()
        print("Клик по кнопке поиска")

    def click_address_icon(self):
        self.get_address_icon().click()
        print("Клик по иконке пункта выдачи")


    def click_delivery_address(self):
        self.get_delivery_address().click()
        print("Клик по адресу доставки")


    def click_confirm_address(self):
        self.get_confirm_address().click()
        print("Клик по кнопке подтверждения адреса доставки")



    #Methods

    def search_delivery_address(self):
        self.visible_map()
        self.input_field_address()
        self.click_search_address_button()
        self.click_delivery_address()
        self.click_confirm_address()

