import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser, base_url):
    browser.get(base_url)
    assert "Your Store" in browser.title
    browser.find_element(By.CLASS_NAME, "dropdown")
    browser.find_element(By.CSS_SELECTOR, "#search")
    browser.find_element(By.XPATH, "//*[@id='form-currency']/div/a/span").click()
    meny_currency = browser.find_element(By.XPATH, "//*[@id='form-currency']/div/ul")
    meny_currency.find_element(By.PARTIAL_LINK_TEXT, "€ Euro")
    meny_currency.find_element(By.PARTIAL_LINK_TEXT,  "£ Pound Sterling")
    meny_currency.find_element(By.PARTIAL_LINK_TEXT, "$ US Dollar")


def test_cataloge(browser, base_url):
    browser.get(base_url + "/en-gb/catalog/")
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
    browser.get(base_url + "/en-gb/catalog/")
    browser.find_element(By.LINK_TEXT, "Continue").click()


def test_card_of_goods(browser, base_url):
    browser.get(base_url + "/en-gb/product/desktops/mac/imac")
    browser.find_element(By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(1) > div > a > img")
    browser.find_element(By.CSS_SELECTOR, "#button-cart").click()
    browser.find_element(By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > "
                                          "div.rating > p > span:nth-child(1) > i").click()
    hoverable = browser.find_element(By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > "
                                          "form > div > button:nth-child(1)")
    ActionChains(browser)\
        .move_to_element(hoverable)\
        .perform()
    browser.find_element(By.ID, "input-quantity")


def test_administration(browser, base_url):
    login = 'user'
    password = 'bitnami'
    browser.get(base_url + "administration/")
    browser.find_element(By.CSS_SELECTOR, "#content > div > div > div > div > div.card-header")
    browser.find_element(By.CSS_SELECTOR, '#form-login > div.text-end > button').click()
    browser.find_element(By.CSS_SELECTOR, '#alert')
    name = browser.find_element(By.ID, 'input-username')
    password_ = browser.find_element(By.ID, 'input-password')
    name.send_keys('89188085879')
    password_.send_keys('123')
    name.clear()
    password_.clear()
    name.send_keys(login)
    password_.send_keys(password)
    browser.find_element(By.CSS_SELECTOR, '#form-login > div.text-end > button').click()
    button = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#nav-profile > a > img')))
    button.click()
    browser.find_element(By.CSS_SELECTOR, '#nav-profile > ul')
    browser.find_element(By.CSS_SELECTOR, '#nav-logout > a')


def test_registration(browser, base_url):
    browser.get(base_url + "/index.php?route=account/register")
    browser.find_element(By.ID, 'content')
    assert browser.find_element(By.CSS_SELECTOR, '#content > h1').text == 'Register Account'
    browser.find_element(By.NAME, 'firstname').send_keys('Вася')
    browser.find_element(By.NAME, 'lastname').send_keys('Иванов')
    browser.find_element(By.NAME, 'email').send_keys('vas@mail.ru')
    browser.find_element(By.NAME, 'password').send_keys('VasVas234.')
    browser.find_element(By.NAME, 'agree').click()
    browser.find_element(By.CSS_SELECTOR, '#form-register > div > button')


def test_add_to_cart(browser, base_url):
    browser.get(base_url)
    browser.execute_script("window.scrollBy(0, 800)")
    tovar = browser.find_element(By.CSS_SELECTOR, '#content > '
                                                  'div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 >'
                                                  ' div:nth-child(1) > div > div.content > div > h4 > a')
    price = browser.find_element(By.CSS_SELECTOR, '#content >'
                                                  ' div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 >'
                                                  ' div:nth-child(1) > div > div.content > div > div > span.price-new')
    time.sleep(6)
    browser.find_element(By.CSS_SELECTOR, '#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 '
                                          '> div:nth-child(1) > '
                                          'div > div.content > form > div > button:nth-child(1)').click()

    browser.execute_script("arguments[0].scrollIntoView(true);",
                           browser.find_element(By.CSS_SELECTOR, '#header-cart > div > button'))
    time.sleep(6)
    browser.find_element(By.CSS_SELECTOR, '#header-cart > div > button').click()
    tovar_v_korzine = browser.find_element(By.CSS_SELECTOR, '#header-cart > div > ul > li > '
                                                            'table > tbody > tr > td.text-start > a')
    price_v_korzine = browser.find_element(By.CSS_SELECTOR, '#header-cart > div > ul > li > '
                                                            'table > tbody > tr > td:nth-child(4)')
    assert tovar.text == tovar_v_korzine.text
    assert price.text == price_v_korzine.text


def test_change_currency(browser, base_url):
    browser.get(base_url)
    browser.find_element(By.XPATH, "//*[@id='form-currency']/div/a/span").click()
    meny_currency = browser.find_element(By.XPATH, "//*[@id='form-currency']/div/ul")
    meny_currency.find_element(By.PARTIAL_LINK_TEXT, "€ Euro").click()
    text1 = browser.find_element(By.CSS_SELECTOR, "#form-currency > div > a > strong").text
    browser.find_element(By.CSS_SELECTOR, '#narbar-menu > ul > li:nth-child(1) > a').click()
    browser.find_element(By.CSS_SELECTOR, '#narbar-menu > ul > li:nth-child(1) > div '
                                          '> div > ul > li:nth-child(2) > a').click()
    text2 = browser.find_element(By.CSS_SELECTOR, '#product-list > div > div > div.content '
                                                  '> div > div > span.price-new').text
    assert text1 in text2










