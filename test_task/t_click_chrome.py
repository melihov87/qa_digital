from time import sleep
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Задание 3. Клик по кнопке
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
driver.maximize_window()
sleep(2)

for i in range(5):
    but_push = driver.find_element(By.XPATH, "//button[contains(@onclick, 'addElement()')]")
    but_push.click()

delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print(f"Размер списка кнопок Delete: {len(delete_buttons)}")
sleep(3)
print('Задание 3. Клик по кнопке - ВЫПОЛНЕНО!')

# Задание 4. Клик по кнопке без ID
driver.get("http://uitestingplayground.com/dynamicid")
driver.maximize_window()
sleep(5)

for i in range(3):
    but_push2 = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    but_push2.click()
print('Задание 4. Клик по кнопке без ID - ВЫПОЛНЕНО!')
sleep(3)

# Задание 5. Клик по кнопке с CSS-классом
driver.get("http://uitestingplayground.com/classattr")
driver.maximize_window()


but_push_blue = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
but_push_blue.click()
sleep(2)
keyboard.press_and_release('enter')
sleep(2)

but_push_blue = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
but_push_blue.click()
sleep(2)
keyboard.press_and_release('enter')
sleep(2)

but_push_blue = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
but_push_blue.click()
sleep(2)
keyboard.press_and_release('enter')
sleep(2)
print('Задание 5. Клик по кнопке с CSS-классом - ВЫПОЛНЕНО!')
sleep(3)

# Задание 6. Модальное окно
driver.get("http://the-internet.herokuapp.com/entry_ad")
driver.maximize_window()
sleep(2)

driver.find_element(By.CLASS_NAME, "modal-footer").click()
sleep(2)
print('Задание 6. Модальное окно - ВЫПОЛНЕНО!')
sleep(3)

# Задание 7. Поле ввода
driver.get("http://the-internet.herokuapp.com/inputs")
driver.maximize_window()
sleep(2)

input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_field.send_keys("1000")
sleep(2)
input_field.clear()
sleep(2)
input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_field.send_keys("999")
print('Задание 7. Поле ввода - ВЫПОЛНЕНО!')
sleep(3)

# Задание 8. Форма авторизации
driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep(2)

enter_name = driver.find_element(By.ID, "username")
enter_name.send_keys("tomsmith")
sleep(2)
enter_password = driver.find_element(By.ID, "password")
enter_password.send_keys("SuperSecretPassword!")
sleep(2)
enter_login = driver.find_element(By.CLASS_NAME, "radius").click()
print('Задание 8. Форма авторизации - ВЫПОЛНЕНО!')
sleep(2)
