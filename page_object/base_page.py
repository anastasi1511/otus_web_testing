from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.actions = ActionChains(driver)
        self.logger = driver.logger
        self.class_name = type(self).__name__

    def open(self, url):
        self.logger.debug('%s: Opening url: %s' % (self.class_name, url))
        self.driver.get(url)

    def click(self, locator):
        self.logger.debug('%s: Clicking element: %s' % (self.class_name, str(locator)))
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input(self, locator, value):
        self.logger.debug('%s: Input %s in input %s' % (self.class_name, value, locator))
        find_field = self.wait.until(EC.element_to_be_clickable(locator))
        find_field.click()
        find_field.clear()
        find_field.send_keys(value)

    def is_present(self, locator):
        self.logger.debug('%s: Check if element %s is present' % (self.class_name, str(locator)))
        return self.wait.until(EC.visibility_of_element_located(locator))







