import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.admins_page import AdminsPage
from page_object.user_page import UserPage
from page_object.url import Urls
from page_object.reg_page import RegPage
from page_object.currency import Currency
from page_object.main_page import MainPage
from page_object.card_of_goods import CardGood
from helpers import (random_string, random_phone, create_random_user, random_email, create_random_name_of_good,
                     create_random_model)


@allure.title('Главный экран')
def test_main_page(browser, base_url):
    browser.get(base_url)
    assert "Your Store" in browser.title
    MainPage(browser).search()
    MainPage(browser).main_meny()
    MainPage(browser).feautured_product_name()
    browser.execute_script("window.scrollBy(0, 600)")
    time.sleep(2)
    MainPage(browser).feautured_product_click()


@allure.title('Каталог товаров')
def test_cataloge(browser, base_url):
    browser.get(Urls(base_url).url_cataloge())
    browser.find_element(By.CSS_SELECTOR, "#column-left").find_element(By.CSS_SELECTOR,
                                                                       "#column-left > div.list-group.mb-3")
    browser.find_element(By.PARTIAL_LINK_TEXT, "Desktops (").click()
    browser.find_element(By.PARTIAL_LINK_TEXT, "Laptops & Notebooks (").click()
    browser.find_element(By.PARTIAL_LINK_TEXT, "Components (").click()
    browser.find_element(By.PARTIAL_LINK_TEXT, "Tablets (").click()
    browser.find_element(By.PARTIAL_LINK_TEXT, "Software (").click()
    browser.find_element(By.PARTIAL_LINK_TEXT, "Phones & PDAs (").click()
    browser.find_element(By.PARTIAL_LINK_TEXT, "Cameras (").click()
    browser.find_element(By.PARTIAL_LINK_TEXT, "MP3 Players (").click()
    browser.get(Urls(base_url).url_cataloge())
    browser.find_element(By.LINK_TEXT, "Continue").click()


@allure.title('Действия в карточке товара')
def test_card_of_goods(browser, base_url):
    browser.get(base_url)
    browser.execute_script("window.scrollBy(0, 800)")
    time.sleep(3)
    MainPage(browser).feautured_product_click()
    browser.find_element(By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(1) > div > a > img")
    CardGood(browser).add_to_card()
    CardGood(browser).add_to_favor()
    hoverable = browser.find_element(By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > "
                                          "form > div > button:nth-child(1)")
    ActionChains(browser)\
        .move_to_element(hoverable)\
        .perform()
    browser.find_element(By.ID, "input-quantity")


@allure.title('Авторизация под администратором')
def test_administration_login(browser, base_url, admin_login, admin_password):
    browser.get(Urls(base_url).url_admin())
    UserPage(browser).login_button()
    UserPage(browser).alert()
    UserPage(browser).login(random_phone(), random_string())
    UserPage(browser).alert()
    UserPage(browser).login_clear()
    UserPage(browser).password_clear()
    UserPage(browser).login(admin_login, admin_password)
    button = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#nav-profile > a > img')))
    button.click()
    AdminsPage(browser).profile()
    AdminsPage(browser).logout()


@allure.title('Регистрация')
def test_registration(browser, base_url):
    browser.get(Urls(base_url).url_reg())
    browser.find_element(By.ID, 'content')
    assert RegPage(browser).title() == 'Register Account'
    RegPage(browser).registation_2agree(create_random_user()["name"], create_random_user()["last_name"],
                                        random_email(), random_string())


@allure.title('Добавление товара')
def test_add_to_cart(browser, base_url):
    browser.get(base_url)
    browser.execute_script("window.scrollBy(0, 800)")
    time.sleep(3)
    tovar = MainPage(browser).feautured_product_name()
    MainPage(browser).feautured_product_click()
    CardGood(browser).add_to_card()
    time.sleep(6)
    price = CardGood(browser).price()
    CardGood(browser).bucket()
    browser.execute_script("arguments[0].scrollIntoView(true);",
                           browser.find_element(By.CSS_SELECTOR, '#header-cart > div > button'))
    time.sleep(6)
    tovar_after_vibor = CardGood(browser).tovar_v_korzine()
    price_after_vibor = CardGood(browser).price_v_korzine()
    assert tovar == tovar_after_vibor
    assert price == price_after_vibor


@allure.title('Смена валюты')
def test_change_currency(browser, base_url):
    browser.get(base_url)
    Currency(browser).open_meny()
    Currency(browser).close_meny()
    Currency(browser).euro()
    text1 = Currency(browser).cur_text()
    browser.find_element(By.CSS_SELECTOR, '#narbar-menu > ul > li:nth-child(1) > a').click()
    browser.find_element(By.CSS_SELECTOR, '#narbar-menu > ul > li:nth-child(1) > div '
                                          '> div > ul > li:nth-child(2) > a').click()
    text2 = browser.find_element(By.CSS_SELECTOR, '#product-list > div > div > div.content '
                                                  '> div > div > span.price-new').text
    assert text1 in text2


@allure.title('Добавление нового товара в разделе админа')
def test_admin_add_new_good(browser, base_url, admin_login, admin_password):
    browser.get(Urls(base_url).url_admin())
    UserPage(browser).login(admin_login, admin_password)
    time.sleep(2)
    add_new_good = AdminsPage(browser)
    add_new_good.menu_catalog()
    add_new_good.go_to_products()
    add_new_good.add_button_plus()
    add_new_good.add_new_good(create_random_name_of_good(), create_random_model(), random_string())
    add_new_good.save_button()


@allure.title('Добавление нового товара и удаление в разделе админа')
def test_admin_add_new_good_and_delete(browser, base_url, admin_login, admin_password):
    browser.get(Urls(base_url).url_admin())
    UserPage(browser).login(admin_login, admin_password)
    time.sleep(2)
    name_of_good = create_random_name_of_good()
    add_new_and_delete = AdminsPage(browser)
    add_new_and_delete.menu_catalog()
    add_new_and_delete.go_to_products()
    add_new_and_delete.add_button_plus()
    add_new_and_delete.add_new_good(name_of_good, create_random_model(), random_string())
    add_new_and_delete.go_to_products()
    add_new_and_delete.filter_by_name(name_of_good)
    add_new_and_delete.delete_new_good()











