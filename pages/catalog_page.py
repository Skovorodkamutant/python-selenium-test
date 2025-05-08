import time
from argparse import Action

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Catalog_page(Base):
    #Класс для каталога

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    all_filters_button = "//div[@class='dropdown-filter j-show-all-filtres']"
    price_field = "//input[@name='endN']"
    radiobutton_delivery = "(//span[@class='radio-with-text__text'])[4]"
    list_input = "//div[@class='filter__input-search input-search input-search--gray']//child::input"
    checkbox = "//span[text()='Аккумулятор для квадрокоптера']"
    present_button = "//button[text()=' Показать ']"
    select_product_button="(//div[@class='product-card__wrapper']/child::div[@class='product-card__bottom-wrap']/child::p[@class='product-card__order-wrap']/child::a/child::span[text()='Послезавтра'])[1]"
    cart_button = "//span[@class='navbar-pc__notify']"
    cookies_button = "//button[text()='Окей']"
    #product_name = "(//span[contains(text(),'QualityPlus')])[1]"
    cart_header = "//h1[@class='basket-section__header basket-section__header--main active']"
    price = "//ins[contains(text(), '265')]"



    # Getters


    def get_all_filters_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.all_filters_button)))

    def get_price_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_field)))

    def get_radiobutton_delivery(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.radiobutton_delivery)))

    def get_list_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.list_input)))

    def get_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox)))

    def get_present_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.present_button)))

    def get_select_product_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_cookies_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cookies_button)))

    # def get_product_name(self):
    #     return WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, self.product_name)))


    def get_cart_header(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_header)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price))).text

    # Actions
    def click_all_filters_button(self):
        self.get_all_filters_button().click()
        print("Кликнули по кнопке всех фильтров")

    def clear_price_field(self):
        self.get_price_field().clear()
        print("Очистили поле цены")

    def input_price_field(self):
        self.get_price_field().send_keys("1000")
        print("Ввели верхнюю границу цены")

    def click_radiobutton_delivery(self):
        self.get_radiobutton_delivery().click()
        print("Кликнули по радиобаттону срока доставки")

    def input_list_input(self):
        self.get_list_input().send_keys("аккумулятор")
        print("Значение товара введено в поле")

    def click_checkbox(self):
        self.get_checkbox().click()
        print("Клик по чекбоксу товара")

    def click_present_button(self):
        self.get_present_button().click()
        print("Клик по кнопке 'Показать'")

    def click_select_product_button(self):
        self.get_select_product_button().click()
        print("Клик по кнопке 'Послезавтра'")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("открываем корзину")

    def click_cookies_button(self):
        self.get_cookies_button().click()
        print("Закрыть сообщение с куки")



    # Methods

    def use_filter(self):
        # выбор товара в фильтре, помещение товара в корзину, переход в корзину
        self.get_current_url()
        self.click_all_filters_button()
        self.clear_price_field()
        self.input_price_field()
        self.click_radiobutton_delivery()
        self.input_list_input()
        self.driver.implicitly_wait(1)
        self.click_checkbox()
        self.click_present_button()

    def select_product(self):
        self.click_cookies_button()
        assert self.get_price() == "265 ₽"
        print("Цена корректна")
        self.click_select_product_button()
        self.click_cart_button()
        self.assert_word(self.get_cart_header(), "Корзина")

