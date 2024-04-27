from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def browser():
    driver = uc.Chrome()
    driver.get("https://www.letu.ru/")
    driver.maximize_window()
    return driver


def menu(driver):
    menu_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div/div/div[2]/div[1]/button/span/span')))
    ActionChains(driver).click(menu_button).perform()

    tehnika_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/browse/tehnika"]')))
    ActionChains(driver).click(tehnika_button).perform()

    tehdom_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'splide08-slide02')))
    ActionChains(driver).click(tehdom_button).perform()
    sleep(2)
    driver.execute_script("window.scrollBy(0, 700);")
    sleep(2)


def product(driver):
    element1 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//img[@alt="Умная колонка Станция Лайт"]')))
    ActionChains(driver).move_to_element(element1).perform()
    element1_incart = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div[1]/a/div[9]/div/div/button[2]')
    ActionChains(driver).click(element1_incart).perform()
    element1_incart1 = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div/div[4]/button')))
    ActionChains(driver).click(element1_incart1).perform()
    close_el1 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/button')))
    ActionChains(driver).click(close_el1).perform()
    sleep(2)
    driver.execute_script("window.scrollBy(0, 700);")

    element2 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/product/polaris-utyug-pir-2821ak-3m/146800126"]')))
    ActionChains(driver).click(element2).perform()
    element2_incart = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="content-wrap"]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div[1]/div[4]/div')))
    ActionChains(driver).click(element2_incart).perform()

    cart_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/cart"]')))
    ActionChains(driver).click(cart_button).perform()


def cart(driver):
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


def start_shop():
    driver = browser()
    menu(driver)
    product(driver)
    cart(driver)
    driver.quit()


start_shop()
