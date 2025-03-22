import keyboard
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from  datetime import datetime

# options = uc.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless=new")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
#
# driver = uc.Chrome(options=options)

start_test = datetime.now()
driver = uc.Chrome()
driver.get("https://www.ozon.ru/")
driver.maximize_window()


# Куки ОК
try:
    cookies_ozon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'gd1_11.b2122-a0.b2122-b5.b2122-a4'))
    )
    cookies_ozon.click()
    print('1) Куки ОК')
except TimeoutException:
    print("1) Элемент не найден, выполняем код дальше.")

# Нажимаю "Войти"
enter_account = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'qca4_48.c20-a.c20-a1'))
)
enter_account.click()
print('2) Окно регистрации открыто')

enter_account2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'cn1a_48.b2122-a0.b2122-b1.b2122-a4'))
)
enter_account2.click()

# Закрываю окно "Войти"
close_account = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'b6026-b1.b6026-a7.ag023-a0.ag023-a5.ag023-a2'))
)
close_account.click()
print('3) Окно регистрации закрыто')

# Нажимаю на "Заказы"
open_orders = driver.find_element(By.CLASS_NAME, 'm0_16.b7124-a.b7124-a5.tsBodyControl500Medium')
open_orders.click()
print('4) Окно заказов открыто')

# Переключаюсь на вторую вкладке, чтобы закрылась вторая вкладка
driver.switch_to.window(driver.window_handles[1])
print('5) Переход на вторую вкладку выполнен')

# Закрываю вторую вкладку
driver.close()
print('6) Вторая вкладка закрыта')

# Активирую первую вкладку
driver.switch_to.window(driver.window_handles[0])
print('7) Первая вкладка активна')

# Обновляю страницу
driver.refresh()
print('8) Страница обновлена')

# Делаю прокрутку в самый низ страницы
scroll = 8
for i in range(scroll):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

print('9) Прокрутка выполнена')

# Нажимаю на раздел Jobs
open_jobs = driver.find_element(By.XPATH, '//a[@href="https://job.ozon.ru/?perehod=footer"]')
open_jobs.click()
print('10) Переход в jobs выполнен')

# Переключаюсь на вторую вкладке, чтобы закрылась вторая вкладка
driver.switch_to.window(driver.window_handles[1])
print('11) Переход на вторую вкладку выполнен')

# Закрываю вторую вкладку
driver.close()
print('12) Вторая вкладка закрыта')

# Активирую первую вкладку
driver.switch_to.window(driver.window_handles[0])
print('13) Первая вкладка активна')

# Делаю прокрутку в самый верх страницы
driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
print('14) Прокрутка вверх выполнена')

# Нажимаю на кнопку "Везде"
everywhere = driver.find_element(By.CSS_SELECTOR, "span[title='Везде']")
everywhere.click()
sleep(2)
print('17) Окно выбора места поиска открыто')

# Закрываю окно "Везде"
close_search = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'b6026-b1.b6026-a7.ag023-a0.ag023-a5.ag023-a2'))
)
close_search.click()
print('18) Окно выбора места поиска закрыто')
print('19) ТЕСТ ВЫПОЛНЕН!')
stop_test = datetime.now()
print(stop_test - start_test)
