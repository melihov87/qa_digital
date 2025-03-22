import ssl
import logging
from time import sleep
from datetime import datetime
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Отключение проверки SSL-сертификатов
ssl._create_default_https_context = ssl._create_unverified_context

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Функция для ожидания кликабельного элемента
def wait_and_click(driver, by, selector, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, selector)))
        element.click()
        logging.info(f"Элемент найден и кликнут: {selector}")
    except TimeoutException:
        logging.warning(f"Элемент не найден: {selector}")

# Функция для переключения вкладок
def switch_to_tab(driver, index):
    try:
        driver.switch_to.window(driver.window_handles[index])
        logging.info(f"Переключение на вкладку {index + 1}")
    except IndexError:
        logging.error("Указанный индекс вкладки недоступен.")

# Функция для скроллинга страницы
def scroll_page(driver, direction="down", steps=8, sleep_time=2):
    for _ in range(steps):
        if direction == "down":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        sleep(sleep_time)
    logging.info(f"Страница прокручена {direction}")

def main():
    # Настройки Chrome
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--headless=new")  # Скрытый режим
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Запуск браузера
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    start_test = datetime.now()

    # Открытие сайта
    driver.get("https://www.ozon.ru/")
    logging.info("Сайт Ozon открыт")

    # Взаимодействие с элементами на сайте
    wait_and_click(driver, By.CLASS_NAME, 'gd1_11.b2122-a0.b2122-b5.b2122-a4')  # Куки
    wait_and_click(driver, By.CLASS_NAME, 'qca4_48.c20-a.c20-a1')  # Войти
    wait_and_click(driver, By.CLASS_NAME, 'cn1a_48.b2122-a0.b2122-b1.b2122-a4')  # Закрыть окно Войти
    wait_and_click(driver, By.CLASS_NAME, 'm0_16.b7124-a.b7124-a5.tsBodyControl500Medium')  # Заказы

    # Работа с вкладками
    switch_to_tab(driver, 1)
    driver.close()
    logging.info("Вторая вкладка закрыта")
    switch_to_tab(driver, 0)

    # Обновление страницы и прокрутка
    driver.refresh()
    logging.info("Страница обновлена")
    scroll_page(driver, "down")
    wait_and_click(driver, By.XPATH, '//a[@href="https://job.ozon.ru/?perehod=footer"]')

    # Переход на вкладку Jobs и её закрытие
    switch_to_tab(driver, 1)
    driver.close()
    logging.info("Вкладка Jobs закрыта")
    switch_to_tab(driver, 0)

    # Скроллинг вверх
    scroll_page(driver, "up")

    # Нажатие и закрытие окна "Везде"
    wait_and_click(driver, By.CSS_SELECTOR, "span[title='Везде']")
    sleep(2)
    wait_and_click(driver, By.CLASS_NAME, 'b6026-b1.b6026-a7.ag023-a0.ag023-a5.ag023-a2')

    # Завершение теста
    logging.info("ТЕСТ ВЫПОЛНЕН!")
    stop_test = datetime.now()
    logging.info(f"Время выполнения теста: {stop_test - start_test}")

    # Закрытие браузера
    driver.quit()

if __name__ == "__main__":
    main()
