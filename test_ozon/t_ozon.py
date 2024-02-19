import keyboard
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.ozon.ru/")
driver.maximize_window()
sleep(5)

# обхожу блокировку
driver.refresh()
sleep(10)

# # Куки ОК
# cookies_ozon = driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[2]/div/div/div/button')
# cookies_ozon.click()
# sleep(3)

# Нажимаю "Войти"
enter_account = driver.find_element(By.CSS_SELECTOR, "[data-widget='profileMenuAnonymous']")
enter_account.click()
sleep(3)

# Закрываю окно "Войти"
close_account = driver.find_element(By.XPATH, "//html/body/div[3]/div/div[2]/div/div/button")
close_account.click()
sleep(3)

# Нажимаю на "Заказы"
open_orders = driver.find_element(By.XPATH, '//*[@href="/my/orderlist"]')
open_orders.click()
sleep(5)

# Переключаюсь на вторую вкладке, чтобы закрылась вторая вкладка
driver.switch_to.window(driver.window_handles[1])
sleep(3)

# Закрываю вторую вкладку
driver.close()
sleep(2)

# Активирую первую вкладку
driver.switch_to.window(driver.window_handles[0])

# Обновляю страницу
driver.refresh()
sleep(5)

# Делаю прокрутку в самый низ страницы
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)

# Нажимаю на раздел Jobs
open_jobs = driver.find_element(By.XPATH, '//a[@href="https://job.ozon.ru/?perehod=footer"]')
open_jobs.click()
sleep(3)

# Переключаюсь на вторую вкладке, чтобы закрылась вторая вкладка
driver.switch_to.window(driver.window_handles[1])
sleep(3)

# Закрываю вторую вкладку
driver.close()
sleep(2)

# Активирую первую вкладку
driver.switch_to.window(driver.window_handles[0])
sleep(2)

# Делаю прокрутку в самый верх страницы
driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
sleep(2)

# Нажимаю на кнопку "RUB"
currency = driver.find_element(By.CSS_SELECTOR, '[data-widget="selectedCurrency"]')
currency.click()
sleep(5)

# Закрываю окно "RUB"
currency_close = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div/button")
currency_close.click()
sleep(2)

# Нажимаю на кнопку "Везде"
everywhere = driver.find_element(By.CSS_SELECTOR, "span[title='Везде']")
everywhere.click()
sleep(3)

# Закрываю окно "Везде"
driver.press_and_release('esc')



