from selenium.webdriver.common.by import By


class Currency:

    def __init__(self, browser):
        self.browser = browser

    def open_meny(self):
        self.browser.find_element(By.XPATH, "//*[@id='form-currency']/div/a/span").click()
        self.browser.find_element(By.XPATH, "//*[@id='form-currency']/div/ul")

    def close_meny(self):
        self.browser.find_element(By.XPATH, "//*[@id='form-currency']/div/a/span").click()

    def euro(self):
        self.browser.find_element(By.XPATH, "//*[@id='form-currency']/div/a/span").click()
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '€ Euro').click()

    def usd(self):
        self.browser.find_element(By.XPATH, "//*[@id='form-currency']/div/a/span").click()
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '$ US Dollar').click()

    def pound(self):
        self.browser.find_element(By.XPATH, "//*[@id='form-currency']/div/a/span").click()
        self.browser.find_element(By.PARTIAL_LINK_TEXT, '£ Pound Sterling').click()

    def cur_text(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#form-currency > div > a > strong").text


