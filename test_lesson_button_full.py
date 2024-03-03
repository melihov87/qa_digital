from time import sleep
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()

# Клик по кнопке
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for i in range(5):
    but_push = driver.find_element(By.XPATH, "//button[contains(@onclick, 'addElement()')]")
    but_push.click()

delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print(f"Клик по кнопке - ВЫПОЛНЕНО! Размер списка кнопок Delete: {len(delete_buttons)}.")

# Клик по кнопке без ID
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

for i in range(3):
    but_push2 = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    but_push2.click()
print('Клик по кнопке без ID - ВЫПОЛНЕНО!')

# Клик по кнопке с CSS-классом
driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")

but_push_blue = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
but_push_blue.click()
keyboard.press_and_release('enter')
sleep(2)

but_push_blue = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
but_push_blue.click()
keyboard.press_and_release('enter')
sleep(2)

but_push_blue = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
but_push_blue.click()
keyboard.press_and_release('enter')
sleep(2)
print('Клик по кнопке с CSS-классом - ВЫПОЛНЕНО!')

# Модальное окно
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/entry_ad")

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "modal-footer"))).click()
print('Модальное окно - ВЫПОЛНЕНО!')

# Поле ввода
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_field.send_keys("1000")
input_field.clear()
input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_field.send_keys("999")
print('Поле ввода - ВЫПОЛНЕНО!')

# Форма авторизации
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

enter_name = driver.find_element(By.ID, "username")
enter_name.send_keys("tomsmith")

enter_password = driver.find_element(By.ID, "password")
enter_password.send_keys("SuperSecretPassword!")

enter_login = driver.find_element(By.CLASS_NAME, "radius").click()
print('Форма авторизации - ВЫПОЛНЕНО!')
print('ТЕСТ ВЫПОЛНЕН!')
