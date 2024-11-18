from selenium.webdriver.common.by import By


class RegPage:

    def __init__(self, browser):
        self.browser = browser

    def title(self):
        return self.browser.find_element(By.CSS_SELECTOR, '#content > h1').text

    def registation_2agree(self, first_name, last_name, e_mail, random_password):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.random_password = random_password
        self.browser.find_element(By.NAME, 'firstname').send_keys(self.first_name)
        self.browser.find_element(By.NAME, 'lastname').send_keys(self.last_name)
        self.browser.find_element(By.NAME, 'email').send_keys(self.e_mail)
        self.browser.find_element(By.NAME, 'password').send_keys(self.random_password)
        self.browser.find_element(By.ID, 'input-newsletter').click()
        self.browser.find_element(By.NAME, 'agree').click()
        self.browser.find_element(By.CSS_SELECTOR, '#form-register > div > button').click()




