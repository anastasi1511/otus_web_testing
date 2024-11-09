from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, browser):
        self.browser = browser

    def search(self):
        self.browser.find_element(By.CSS_SELECTOR, "#search")

    def main_meny(self):
        self.browser.find_element(By.ID, "menu")

    def feautured_product_name(self, index=0):
        feauture_product = self.browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a")[index]
        product_name = feauture_product.text
        return product_name

    def feautured_product_click(self, index=0):
        self.browser.find_elements(By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a")[index].click()






