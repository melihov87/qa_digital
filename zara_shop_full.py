import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import Workbook
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc


driver = uc.Chrome()
driver.maximize_window()
driver.get("https://www.zara.com/")
ac = ActionChains(driver)

# Открываю поле выбора языка
lang_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'downshift-1-toggle-button'))).click()

# Выбираю английский язык
us_button = driver.find_element(By.ID, 'downshift-1-item-1').click()

# Вход на сайт, после выбора языка и региона
driver.find_element(By.CLASS_NAME, 'zds-button__lines-wrapper').click()
print('Ура! Я на сайте!')


# Открываю меню для женщин
woomen_button = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, "slider-spot-universes-bar__item--selected")))
woomen_button.click()
print('Меню для женщин открылось!')

# Выбираю жилетки
wais_button = driver.find_element(By.XPATH, '//a[@href="https://www.zara.com/me/en/woman-outerwear-vests-l1204.html"]')
ac.pause(3).scroll_to_element(wais_button).click(wais_button).perform()
print('Каталог с жилетками открыт')

# Меняю отображение товаров на странице
zoom_button = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="theme-app"]/div/div/header/div[4]/div[2]/button[2]'))).click()
print('Отображение товаров изменено')

# ================================================================
# Сохраняем список товаров в xls и в json
product_elements = driver.find_elements(By.CLASS_NAME, 'product-grid-product')
wb = Workbook()
ws = wb.active
ws.append(["Product Name", "Price", "URL"])

for product in product_elements:
    product_name = product.find_element(By.CLASS_NAME, 'product-grid-product-info__name').text
    product_price = product.find_element(By.CLASS_NAME, 'price-current__amount').text
    product_url = product.find_element(By.CSS_SELECTOR, 'a.product-grid-product__link').get_attribute('href')
    ws.append([product_name, product_price, product_url])

wb.save("products.xlsx")


products = []

for product in product_elements:
    product_name = product.find_element(By.CLASS_NAME, 'product-grid-product-info__name').text
    product_price = product.find_element(By.CLASS_NAME, 'price-current__amount').text
    product_url = product.find_element(By.CSS_SELECTOR, 'a.product-grid-product__link').get_attribute('href')
    products.append({
        "Product Name": product_name,
        "Price": product_price,
        "URL": product_url
    })

with open("products.json", "w") as json_file:
    json.dump(products, json_file, indent=4)

print('Товары сохранены')
# ==================================================================


# Первый товар=============================================
zh1 = driver.find_element(By.XPATH, '//a[@href="https://www.zara.com/me/en/short-tailored-waistcoat-p09929126.html"]').click()
# Параметры-----------------------------
button_color1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/article/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/ul/li[1]'))).click()
button_size1 = driver.find_element(By.ID, 'product-size-selector-311287653-item-3').click()
button_add1 = driver.find_element(By.XPATH, '//*[@id="main"]/article/div[2]/div[1]/div[2]/div/div[3]').click()
driver.back()
print('Первый товар куплен')


# Второй товвар===========================================
zh2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-productid="332212623"]'))).click()
# Параметры---------------------------
button_size2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'product-size-selector-332212623-item-0'))).click()
button_add2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/article/div[2]/div[1]/div[2]/div/div[3]/div'))).click()
driver.back()
print('Второй товар куплен')

ac.key_down(Keys.PAGE_DOWN).pause(1).perform()
ac.key_down(Keys.PAGE_DOWN).pause(1).perform()
ac.key_down(Keys.PAGE_DOWN).pause(1).perform()
ac.key_down(Keys.PAGE_DOWN).pause(1).perform()
ac.key_down(Keys.PAGE_DOWN).pause(3).perform()


# Третий товар=========================================================
zh3 = driver.find_element(By.CSS_SELECTOR, '[data-productid="322677493"]')
zh3.click()
# Параметры------------------------------------------------------------
button_size3 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'product-size-selector-322677493-item-3'))).click()
button_add3 = driver.find_element(By.CLASS_NAME, 'zds-button__lines-wrapper').click()
driver.back()
print('Третий товар куплен')

# Перехожу в корзину
cart_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="theme-app"]/div/div/header/div[3]/a[3]'))).click()

final_sum_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/article/div[2]/div/div/div/div[2]/section/div[2]/div/span[2]')))
final_sum_text = final_sum_element.text.strip('EUR').strip()

final_sum = float(final_sum_text)

actual_total = 61.85

if final_sum == actual_total:
    print(f'Сумма заказа в корзине {final_sum_text} EUR совпадает с актуальной {actual_total} EUR')
else:
    print(f'Сумма заказа и сумма товаров в корзине не совпадают, стоимость заказа: {final_sum_text} EUR')
