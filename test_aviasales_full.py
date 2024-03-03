from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.aviasales.ru/")
driver.maximize_window()

# установка курсора в поле "Откуда"
field_where_from = driver.find_element(By.ID, "avia_form_origin-input")
field_where_from.click()
print('1) Курсор установлен в поле Откуда')

# установка курсора в поле "Куда"
field_where = driver.find_element(By.ID, "avia_form_destination-input")
field_where.click()
print('2) Курсор установлен в поле Куда')

# установка курсора в поле "Когда"
field_when = driver.find_element(By.CSS_SELECTOR, "[data-test-id='start-date-field']")
field_when.click()
print('3) Курсор установлен в поле Когда')

# установка курсора в поле "Обратно"
field_black = driver.find_element(By.CSS_SELECTOR, "[data-test-id='end-date-field']")
field_black.click()
print('4) Курсор установлен в поле Обратно')

# Клик на логотип
button_avia = driver.find_element(By.CSS_SELECTOR, "[data-test-id='logo']")
button_avia.click()

# Чек-бокс "Открыть Ostrovok.ru в новой вкладке"
ostrovok = driver.find_element(By.CSS_SELECTOR, "[data-test-id='no-cashback-label']")
ostrovok.click()
print('5) Включено')
ostrovok.click()
print('6) Выключено')

# Клик по кнопке "Найти билеты"
find_tickets = driver.find_element(By.CSS_SELECTOR, "[data-test-id='form-submit']")
find_tickets.click()
print('7) Кнопка Найти билеты нажата')
print('6) ТЕСТ ВЫПОЛНЕН!')
