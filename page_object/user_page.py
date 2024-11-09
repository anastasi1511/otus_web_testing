from selenium.webdriver.common.by import By


class UserPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.find_element(By.ID, 'input-username').send_keys(username)
        self.browser.find_element(By.ID, 'input-password').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '#form-login > div.text-end > button').click()

    def login_button(self):
        button = self.browser.find_element(By.CSS_SELECTOR, '#form-login > div.text-end > button').click()
        return button

    def alert(self):
        self.browser.find_element(By.CSS_SELECTOR, '#alert')

    def login_clear(self):
        self.browser.find_element(By.ID, 'input-username').clear()

    def password_clear(self):
        self.browser.find_element(By.ID, 'input-password').clear()



