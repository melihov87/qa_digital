from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup


def browser():
    driver = webdriver.Firefox()
    driver.get("https://www.letu.ru/")
    driver.maximize_window()
    return driver


def menu(driver):
    menu_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div/div/div[2]/div[1]/button/span/span')))
    menu_button.click()

    tehnika_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/browse/tehnika"]')))
    tehnika_button.click()

    tehdom_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'splide08-slide02')))
    tehdom_button.click()

    driver.execute_script("window.scrollBy(0, 300);")


def product(driver):
    element1 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//img[@alt="Умная колонка Станция Лайт"]')))
    element1.click()
    element1_incart = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '//*[@id="content-wrap"]/div[2]/div/div/div/div[1]/div[2]/div['
                                                                                      '3]/div[2]/div[1]/div[4]/div/button/span/span')))
    element1_incart.click()
    driver.back()
    sleep(5)

    driver.execute_script("window.scrollBy(0, 700);")

    element2 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/product/polaris-utyug-pir-2821ak-3m/146800126"]')))
    element2.click()

    element2_incart = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="content-wrap"]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div[1]/div[4]/div')))
    element2_incart.click()

    cart_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/cart"]')))
    cart_button.click()
    sleep(5)


def cart_sum(driver):
    cart_summary = ('<div data-at-price-sum="" class="cart-summary-item__value'
                    'skeleton-loading-item"><span>9&nbsp;689 ₽</span></div>')
    soup = BeautifulSoup(cart_summary, 'html.parser')
    cart_price_tag = soup.find('span')
    cart_price_text = cart_price_tag.get_text()
    cart_price = int(cart_price_text.replace('\xa0', '').split(' ')[0])
    your_price = 9689
    if cart_price == your_price:
        print("The amounts match!")
    else:
        print("The amounts do not match!")


def start_test():
    driver = browser()
    menu(driver)
    product(driver)
    cart_sum(driver)
    driver.quit()


start_test()
