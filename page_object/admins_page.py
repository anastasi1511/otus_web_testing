import time

from selenium.webdriver.common.by import By


class AdminsPage:

    def __init__(self, browser):
        self.browser = browser

    def profile(self):
        self.browser.find_element(By.CSS_SELECTOR, '#nav-profile > ul')

    def logout(self):
        self.browser.find_element(By.CSS_SELECTOR, '#nav-logout > a')

    def add_new_good(self, product_name, meta_tag_title, model, keyword):
        self.browser.find_element(By.ID, 'menu-catalog').click()
        time.sleep(2)
        self.browser.find_element(By.LINK_TEXT, 'Products').click()
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR, '#content > div.page-header > div > div > a').click()
        self.browser.find_element(By.ID, 'input-name-1').send_keys(product_name)
        self.browser.find_element(By.ID, 'input-meta-title-1').send_keys(meta_tag_title)
        self.browser.find_element(By.LINK_TEXT, 'Data').click()
        self.browser.find_element(By.ID, 'input-model').send_keys(model)
        self.browser.find_element(By.LINK_TEXT, 'SEO').click()
        self.browser.find_element(By.CSS_SELECTOR, '#input-keyword-0-1').send_keys(keyword)
        self.browser.find_element(By.CSS_SELECTOR, '#content > div.page-header > div > div > button').click()

    def go_to_products(self):
        self.browser.find_element(By.LINK_TEXT, 'Products').click()
        time.sleep(1)

    def delete_new_create_good(self, product_name):
        self.browser.find_element(By.CSS_SELECTOR, '#input-name').send_keys(product_name)
        self.browser.find_element(By.CSS_SELECTOR, '#button-filter').click()
        checkbox = self.browser.find_elements(By.CLASS_NAME, 'form-check-input')
        checkbox[0].click()
        self.browser.find_element(By.CSS_SELECTOR, '#content > div.page-header >'
                                                   ' div > div > button.btn.btn-danger').click()
        self.browser.switch_to.alert.accept()









