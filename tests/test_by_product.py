import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.catalog_page import Catalog_page
from pages.delivery_page import Delivery_page
from pages.main_page import Main_page


def test_select_product():
    #patch = 'C:\\Users\\still\\PycharmProjects\\resource\\geckodriver.exe'
    patch = 'C:\\Users\\still\\PycharmProjects\\resource\\chromedriver.exe'
    s = Service(patch)
    #driver = webdriver.Firefox(service=s)
    driver = webdriver.Chrome(service=s)

    print("Start test")

    mp = Main_page(driver)
    mp.search_product()

    cp = Catalog_page(driver)
    cp.use_filter()
    cp.select_product()

    cap = Cart_page(driver)
    cap.select_pvz()

    dp = Delivery_page(driver)
    dp.search_delivery_address()

    cap.confirm_order()
    cap.open_login_form()

    driver.quit()
