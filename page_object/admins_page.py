import time

import allure
from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class AdminsPage(BasePage):
    PROFILE_ICON = (By.CSS_SELECTOR, '#nav-profile > ul')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#nav-logout > a')
    MENU_CATALOG = (By.ID, 'menu-catalog')
    PRODUCTS_FIELD = (By.LINK_TEXT, 'Products')
    BUTTON_PLUS = (By.CSS_SELECTOR, '#content > div.page-header > div > div > a')
    NAME_FIELD = (By.ID, 'input-name-1')
    META_TAG_FIELD = (By.ID, 'input-meta-title-1')
    DATA_TAB = (By.LINK_TEXT, 'Data')
    MODEL_FIELD = (By.ID, 'input-model')
    SEO_TAB = (By.LINK_TEXT, 'SEO')
    KEYWORD_FIELD = (By.CSS_SELECTOR, '#input-keyword-0-1')
    SAVE_BUTTON = (By.CSS_SELECTOR, '#content > div.page-header > div > div > button')
    FILTER_NAME_FIELD = (By.CSS_SELECTOR, '#input-name')
    FILTER_BUTTON = (By.CSS_SELECTOR, '#button-filter')
    DELETE_BUTTON = (By.CSS_SELECTOR, '#content > div.page-header >'
                                                   ' div > div > button.btn.btn-danger')

    @allure.step('Ecть иконка профайла')
    def profile(self):
        self.is_present(self.PROFILE_ICON)

    @allure.step('Ecть иконка выхода')
    def logout(self):
        self.is_present(self.LOGOUT_BUTTON)

    @allure.step('Клик по полю Каталог в админке')
    def menu_catalog(self):
        self.click(self.MENU_CATALOG)

    @allure.step('Клик по полю Продукты в каталоге')
    def go_to_products(self):
        self.click(self.PRODUCTS_FIELD)

    @allure.step('Клик по кнопке +')
    def add_button_plus(self):
        self.click(self.BUTTON_PLUS)

    @allure.step('Заполнение полей добавления нового товара в каталоге')
    def add_new_good(self, product_name, model, keyword):
        self.input(self.NAME_FIELD, product_name)
        self.input(self.META_TAG_FIELD, product_name)
        self.click(self.DATA_TAB)
        self.input(self.MODEL_FIELD, model)
        self.click(self.SEO_TAB)
        self.input(self.KEYWORD_FIELD, keyword)

    @allure.step('Клик по кнопке Сохранить новый товар в каталоге')
    def save_button(self):
        self.click(self.SAVE_BUTTON)

    @allure.step('Заполнить поле наименование товара в фильтре каталога продуктов')
    def filter_by_name(self, product_name):
        self.input(self.FILTER_NAME_FIELD, product_name)
        self.click(self.FILTER_BUTTON)

    @allure.step('Выделить все товары чекбоксом')
    def checkbox(self):
        checkbox = self.driver.find_elements(By.CLASS_NAME, 'form-check-input')
        checkbox[0].click()
        time.sleep(2)

    @allure.step('Клик по кнопке удаления и ок в аллерте')
    def delete_new_good(self):
        self.click(self.DELETE_BUTTON)
        self.driver.switch_to.alert.accept()









