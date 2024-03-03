import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# Проверяем кнопки на сайте и создаем xls файл с товарами со страницы


def driver():
    browser = uc.Chrome()
    browser.maximize_window()
    browser.get("https://www.wildberries.ru/")
    browser.implicitly_wait(5)
    return browser


def button(browser):
    # Нажимаем на Меню
    menu_site = browser.find_element(By.CSS_SELECTOR, '[data-wba-header-name="Catalog"]')
    ActionChains(browser).move_to_element(menu_site).pause(2).click(menu_site).perform()
    # Нажимаем на Электроника
    el_menu = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-menu-id="4830"]'))
    )
    el_menu.click()
    # Нажимаем на Смартфоны и телефоны
    tel_smart = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/catalog/elektronika/smartfony-i-telefony"]'))
    )
    tel_smart.click()
    # Нажимаем на Смартфоны
    smart_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[href="/catalog/elektronika/smartfony-i-telefony/vse-smartfony"]'))
    )
    smart_button.click()
    # Нажимаем на Все фильтры
    filter_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Все фильтры")]'))
    )
    filter_button.click()

    # Кликаем в фильтре на "Apple"
    apple_button = browser.find_element(By.XPATH, '//li[@class="filter__item"]/div/span[contains(text(), "Apple")]')
    ActionChains(browser).pause(1).move_to_element(apple_button).click().perform()


def product(browser):
    # Нажимаем на "Посмотреть"
    show_button = browser.find_element(By.CLASS_NAME, 'filters-desktop__btn-main')
    ActionChains(browser).move_to_element(show_button).click(show_button).perform()

    # Пролистываем до конца страницы, для появления всех товаров
    num_page_downs = 13
    for i in range(num_page_downs):
        ActionChains(browser).pause(1).key_down(Keys.PAGE_DOWN).perform()

    # Карточка товара
    product_cards = browser.find_elements(By.CLASS_NAME, 'product-card')

    # Списки для хранения извлеченных данных
    ids = []
    brands = []
    names = []
    prices = []

    # Проходимся по каждому элементу product-card и извлекаем нужные данные
    for product_card in product_cards:
        # Извлекаем ID товара
        id_element = product_card.get_attribute('data-nm-id')
        ids.append(id_element)

        # Извлекаем бренд товара
        brand_element = product_card.find_element(By.CLASS_NAME, 'product-card__brand').text.strip()
        brands.append(brand_element)

        # Извлекаем название товара
        name_element = product_card.find_element(By.CLASS_NAME, 'product-card__name').text.strip()
        names.append(name_element)

        # Извлекаем цену товара
        price_element = product_card.find_element(By.CLASS_NAME, 'price__lower-price').text.strip()
        prices.append(price_element)

    df = pd.DataFrame({
        'ID': ids,
        'Brand': brands,
        'Name': names,
        'Price': prices
    })

    # Сохранение данных в Excel
    filename = 'wildberries_products.xlsx'
    try:
        df.to_excel(filename, index=False)
        print(f"Product data has been saved to '{filename}'")
    except Exception as e:
        print("Failed to save data to Excel:", e)


def example():
    browser = driver()
    button(browser)
    product(browser)
    browser.quit()


example()
