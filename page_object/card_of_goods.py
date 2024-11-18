from selenium.webdriver.common.by import By


class CardGood:

    def __init__(self, browser):
        self.browser = browser

    def add_to_card(self):
        self.browser.find_element(By.ID, 'button-cart').click()

    def price(self):
        return self.browser.find_element(By.CLASS_NAME, "price-new").text

    def bucket(self):
        self.browser.find_element(By.ID, 'header-cart').click()

    def tovar_v_korzine(self):
        return self.browser.find_element(By.CSS_SELECTOR, '#header-cart > div > ul > li > table > tbody'
                                                          ' > tr > td.text-start > a').text

    def price_v_korzine(self):
        return self.browser.find_element(By.CSS_SELECTOR, '#header-cart > div > ul > li > table > '
                                                          'tbody > tr > td:nth-child(4)').text

    def add_to_favor(self):
        self.browser.find_element(By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > "
                                          "div.rating > p > span:nth-child(1) > i").click()
