
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base



class Cart_page(Base):
    # Класс для функционала Корзины
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    #Locators

    pvz_link = "//div[@class='basket-delivery__choose-address j-btn-choose-address']"
    confirm_order_button = "//button[@class='b-btn-do-order btn-main j-btn-confirm-order']"
    login_link = "(//a[@class='basket-section__link-msg'])[2]"
    phone_form = "//input[@class='input-item']"
    close_push = "//button[@class='tooltip__close']"
    request_code_button = "//button[@id='requestCode']"
    delivery_header = "//h2[@class='geo-block__info-title hide-mobile']"
    delivery_b_address = "//div[@class='b-delivery__address']"
    delivery_day = "//span[@class='good-info__item']"
    price_not_sale = "//div[contains(text(), '271')]"
    price_for_sale = "//div[@class='list-item__price-wallet red-price']"
    final_price = "//span[contains(text(), '271')]"
    code_title = "//h2[@class='login__code-title']"






    #Getters

    def get_delivery_day(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery_day)))

    def get_pvz_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.pvz_link)))

    def get_confirm_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_order_button)))

    def get_login_link(self):
        return WebDriverWait(self.driver, 300).until(
            EC.element_to_be_clickable((By.XPATH, self.login_link)))


    def get_phone_form(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_form)))

    def get_close_push(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.close_push)))

    def get_request_code_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.request_code_button)))

    def get_delivery_header(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery_header)))


    def get_delivery_b_address(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery_b_address)))

    def get_price_not_sale(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_not_sale))).text

    def get_price_for_sale(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_for_sale))).text

    def get_final_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.final_price))).text


    def get_code_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.code_title))).text

    # Actions
    def click_pvz_link(self):
        self.get_pvz_link().click()
        print("Открываем выбор пункта выдачи")

    def click_close_push(self):
        self.get_close_push().click()
        print("Закрыть пуш-сообщение")

    def click_confirm_order(self):
        self.get_confirm_order().click()
        print("Клик на кнопку подтверждения заказа")

    def click_login_link(self):
        self.get_login_link().click()
        print("Клик на ссылку входа")

    def input_phone(self):
        self.get_phone_form().send_keys("0000000000")
        print("Ввод номера телефона")

    def click_request_code_button(self):
        self.get_request_code_button().click()
        print("Получение кода для входа")

    #Methods
    def select_pvz(self):
        #Переход в функционал выбора пункта выдачи
        self.assert_word(self.get_delivery_day(), "Послезавтра")
        self.click_pvz_link()
        self.assert_word(self.get_delivery_header(), "Выберите способ доставки")

    def confirm_order(self):
        #Подтверждение заказа, проверка цен
        #Использовал обычные ассерты для проверки значения цен,
        # т.к. обнаружил, что assert_word именно с ценами ломает тест

        assert self.get_price_not_sale() == "271 ₽"
        print("Цена без скидки корректна")
        assert self.get_price_for_sale() == "265 ₽"
        print("Цена со скидкой WB корректна")
        assert self.get_price_not_sale() == self.get_final_price()
        print("Цена без скидки и цена итого совпадают")
        self.click_close_push()
        self.assert_word(self.get_delivery_b_address(), "Усть-Каменогорск, улица Ломоносова 43/2")

    def open_login_form(self):
        # Переход к функционалу авторизации
        self.click_login_link()
        self.input_phone()
        self.click_request_code_button()
        assert self.get_code_title() == "Откройте уведомление в приложении Wildberries"
        print("Отображается окно для ввода кода подтвержения")


