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


driver = uc.Chrome()
driver.get("https://www.ozon.ru/")
driver.maximize_window()


# Куки ОК
try:
    cookies_ozon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="layoutPage"]/div[2]/div/div/div/button'))
    )
    cookies_ozon.click()
    print('1) Куки ОК')
except TimeoutException:
    print("1) Элемент не найден, выполняем код дальше.")

# Нажимаю "Войти"
enter_account = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="stickyHeader"]/div[3]/div[1]'))
)
enter_account.click()
print('2) Окно регистрации открыто')

# Закрываю окно "Войти"
close_account = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div/button"))
)
close_account.click()
print('3) Окно регистрации закрыто')

# Нажимаю на "Заказы"
open_orders = driver.find_element(By.XPATH, '//*[@href="/my/orderlist"]')
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

# Нажимаю на кнопку "RUB"
currency = driver.find_element(By.CSS_SELECTOR, '[data-widget="selectedCurrency"]')
currency.click()
print('15) Окно валют открыто')

# Закрываю окно "RUB"
currency_close = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div/button")
currency_close.click()
print('16) Окно валют закрыто')

# Нажимаю на кнопку "Везде"
everywhere = driver.find_element(By.CSS_SELECTOR, "span[title='Везде']")
everywhere.click()
print('17) Окно выбора места поиска открыто')

# Закрываю окно "Везде"
driver.press_and_release('esc')
print('18) Окно выбора места поиска закрыто')
print('19) ТЕСТ ВЫПОЛНЕН!')
