import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import time
from selenium.webdriver.common.by import By
from time import sleep
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


@allure.title('Запуск браузера')
@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver: webdriver.Chrome = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def action(driver):
    return ActionChains(driver)


@pytest.fixture(scope="session")
def keys(driver):
    return Keys()


@pytest.fixture(scope="session")
def wd(driver):
    return WebDriverWait(driver, 10)


@allure.title('Открытие сайта Детский мир')
@allure.severity('CRITICAL')
def test_open_detmir(driver):
    driver.get("https://www.detmir.ru/")
    assert "Детский мир" in driver.title


@allure.title('Регион и куки')
def test_geo_cookies(driver, action):
    @allure.step('Нажатие на кнопку "Верно"')
    def click_to_geo():
        geo_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/span[contains(text(), "Верно!")]'))
        )
        action.pause(2).click(geo_click).perform()

    @allure.step('Добавление cookies')
    def add_cookies():
        cookie = {'name': 'DM_CookieNotification', 'value': '0'}
        driver.add_cookie(cookie)
        driver.refresh()
        sleep(3)

    click_to_geo()
    add_cookies()


@allure.title('Баннер в шапке')
def test_click_banner(driver):
    banner_footer = driver.find_element(By.XPATH, '//div[@class="sp gG"]')
    banner_footer.click()
    driver.back()


@allure.title('Клик по логотипу ЗООЗАВР')
def test_logo_pet_products(driver):
    @allure.step('Клик по Товары для животных от Зоозавра')
    def click_logo_pet_products():
        zoo_click_fut = driver.find_element(By.XPATH, '//a[@href="https://zoozavr.ru"]')
        zoo_click_fut.click()

    @allure.step('Сравнение ссылки Зоозавр с открытой')
    def url_pet_products_logo():
        zoo_url_logo = driver.current_url
        zoo_url_parse_logo = urlparse(zoo_url_logo)
        zoo_url_scheme_logo = zoo_url_parse_logo.scheme
        zoo_url_netloc_logo = zoo_url_parse_logo.netloc
        base_url = f'{zoo_url_scheme_logo}://{zoo_url_netloc_logo}/'
        if base_url == 'https://zoozavr.ru/':
            print("Ссылка совпала")
        else:
            print("Ссылка не совпала")
        driver.back()
        sleep(2)

    click_logo_pet_products()
    url_pet_products_logo()


@allure.title('Выбор региона')
def test_choice_region(driver, action):
    @allure.step('Клик по кнопке выбора региона')
    def click_region():
        choice_region_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="P_6 Qb"]'))
        )
        choice_region_click.click()
        time.sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей выбора региона')
    def text_region():
        info_name_region = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//h2[@class="rK HA"]'))
        ).text
        expected_result_region = 'Выбор региона'
        assert info_name_region == expected_result_region, "Регион не совпал"
        time.sleep(2)

    @allure.step('Закрыть окно выбора региона')
    def test_close_window():
        action.send_keys(Keys.ESCAPE).perform()
        sleep(3)

    click_region()
    text_region()
    test_close_window()


@allure.title('Выбор магазина')
def test_choosing_store(driver, action):
    @allure.step('Клик по выбору магазина')
    def click_choosing_store():
        shops_click = driver.find_element(By.XPATH, '(//a[@class="rJ"])[1]')
        action.pause(3).move_to_element(shops_click).click(shops_click).perform()

    @allure.step('Сравнить текст открытой страницы со страницей "Магазины"')
    def text_choosing_store():
        info_name_shops = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        info_name_shops_str = info_name_shops[0:24]
        expected_result_shops = 'Магазины «Детский мир»: '
        if info_name_shops_str == expected_result_shops:
            print('Выбор магазина - Текст совпал')
        else:
            print('Выбор магазина - Текст не совпал')
        driver.back()
        sleep(2)

    click_choosing_store()
    text_choosing_store()


@allure.title('Доставка и оплата')
def test_delivery(driver):
    @allure.step('Клик по Доставка и оплата')
    def click_delivery():
        delivery_click = driver.find_element(By.XPATH, '(//span[@class="rq"])[2]')
        delivery_click.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Доставка и оплата"')
    def text_delivery():
        delivery_click_info = driver.find_element(By.XPATH, '//span[@class="mD"]').text
        delivery_click_info_text = delivery_click_info[0:24]
        expected_result_delivery = 'Доставка и оплата: '
        if delivery_click_info_text == expected_result_delivery:
            print('Доставка и оплата - Текст совпал')
        else:
            print('Доставка и оплата - Текст не совпал')
        driver.back()
        sleep(2)

    click_delivery()
    text_delivery()


@allure.title('Продавать в Детском мире')
def test_sell_detmir(driver):
    @allure.step('Клик по Продавать в Детском мире')
    def click_sell_detmir():
        sell_click = driver.find_element(By.XPATH, '(//a[@class="rJ"])[3]')
        sell_click.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Продавать в Детском мире"')
    def text_sell_detmir():
        sell_click_info = driver.find_element(By.XPATH, '//div[@class="t396__elem tn-elem tn-elem__4854365141661933876993"]').text
        expected_result_sell = 'Продавайте на маркетплейсе\nДетского мира'
        if sell_click_info == expected_result_sell:
            print('Продавать в Детском мире - Текст совпал')
        else:
            print('Продавать в Детском мире - Текст не совпал')
        driver.back()
        sleep(2)

    click_sell_detmir()
    text_sell_detmir()


@allure.title('Обмен и возврат товара')
def test_clik_exchange(driver, action):
    @allure.step('Клик по кнопке "Еще"')
    def click_more():
        more_click = driver.find_element(By.XPATH, '//div[@class="rN"]')
        action.click(more_click).pause(2).perform()

    @allure.step('Клик по обмен и возврат товара')
    def click_exchange():
        exchange_click = driver.find_element(By.XPATH, '(//a[@class="rJ"])[4]')
        exchange_click.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Обмен и возврат товара"')
    def text_exchange():
        exchange_click_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_exchange = 'Обмен и возврат товара'
        if exchange_click_text == expected_result_exchange:
            print('Обмен и возврат товара - Текст совпал')
        else:
            print('Обмен и возврат товара - Текст не совпал')
        driver.back()

    click_more()
    click_exchange()
    text_exchange()


@allure.title('Обратная связь')
def test_clik_feedback(driver, action):
    @allure.step('Клик по кнопке "Еще"')
    def click_more():
        more_click = driver.find_element(By.XPATH, '//div[@class="rN"]')
        action.click(more_click).pause(2).perform()

    @allure.step('Клик по Обратная связь')
    def click_feedback():
        feedback_click = driver.find_element(By.XPATH, '(//li[@class="rm rF ry rn fq rI"])[2]')
        feedback_click.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Обратная связь"')
    def text_feedback():
        feedback_click_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_feedback = 'Обратная связь'
        if feedback_click_text == expected_result_feedback:
            print('Обратная связь - Текст совпал')
        else:
            print('Обратная связь - Текст не совпал')
        driver.back()

    click_more()
    click_feedback()
    text_feedback()


@allure.title('Статус заказа')
def test_order_status(driver, action):
    @allure.step('Клик по Статус заказа')
    def click_order_status():
        status_order_click = driver.find_element(By.XPATH, '//div[@class="fF"]')
        status_order_click.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Входа в аккаунт"')
    def text_order_status():
        status_order_click_text = driver.find_element(By.XPATH, '//h3[@class="TB TD VJ Vz VE"]').text
        expected_result_status_orders = 'Войдите или создайте профиль'
        if status_order_click_text == expected_result_status_orders:
            print('Входа в аккаунт - Текст совпал')
        else:
            print('Входа в аккаунт - Текст не совпал')

    @allure.step('Закрыть окно Входа в аккаунт')
    def test_close_window_account():
        action.send_keys(Keys.ESCAPE).perform()
        sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей "Профиль"')
    def text_hi():
        status_order_profile_text = driver.find_element(By.XPATH, '//div[@class="_6K _6J"]').text
        expected_result_status_profile = 'Привет!'
        if status_order_profile_text == expected_result_status_profile:
            print('Профиль - Текст совпал')
        else:
            print('Профиль - текст не совпал')
        driver.back()

    @allure.step('Закрыть окно выбора региона')
    def test_close_window_account_page():
        action.send_keys(Keys.ESCAPE).perform()
        driver.back()

    click_order_status()
    text_order_status()
    test_close_window_account()
    text_hi()
    test_close_window_account_page()


@allure.title('Открытие Чата')
def test_open_chat(driver, action):
    @allure.step('Клик по иконке Чат')
    def click_chat():
        chat_click = driver.find_element(By.ID, 'button_ChatWidget')
        action.click(chat_click).pause(2).click(chat_click).pause(2).perform()

    @allure.step('Переключение на другой iframe')
    def switch_iframe():
        driver.switch_to.frame(driver.find_element(By.ID, 'hde-iframe'))
        sleep(3)

    @allure.step('Ввод имени в чат')
    def input_name():
        name_input = driver.find_element(By.XPATH, '//input[@placeholder="Имя"]')
        name_input.send_keys('Иван')

    @allure.step('Ввод email в чат')
    def input_email():
        email_input = driver.find_element(By.XPATH, '//input[@placeholder="Э-почта"]')
        email_input.send_keys('ivan@ya.ru')

    @allure.step('Ввод сообщения в чат')
    def input_message():
        message_input = driver.find_element(By.XPATH, '//textarea[@placeholder="Отправить ваш вопрос Ctrl+Enter"]')
        message_input.send_keys('Hello!')

    @allure.step('Клик по чекбоксу')
    def click_on_checkbox():
        check_chat_click = driver.find_element(By.XPATH, '//span[@class="el-checkbox__inner"]')
        check_chat_click.click()

    @allure.step('Отправить сообщение')
    def click_button_send():
        send_message_chat = driver.find_element(By.XPATH, '//button[@class="el-button custom-button-color el-button--info el-button--small is-plain"]')
        send_message_chat.click()

    @allure.step('Закрыть чат')
    def closed_chat():
        close_chat = driver.find_element(By.XPATH, '//div[@class="widget-close"]')
        close_chat.click()
        print('The message has been sent')

    click_chat()
    switch_iframe()
    input_name()
    input_email()
    input_message()
    click_on_checkbox()
    click_button_send()
    closed_chat()


@allure.title('Переключение на другой iframe')
@allure.step('Переключение на другой iframe')
def test_switching(driver):
    driver.switch_to.default_content()


@allure.title('Клик по логотипу')
@allure.step('Клик по логотипу')
def test_click_to_logo(driver):
    logo_click = driver.find_element(By.XPATH, '//a[@class="rY rZ"]')
    logo_click.click()


@allure.title('Профиль')
def test_click_account(driver):
    @allure.step('Клик по Профиль')
    def click_account():
        profile_click = driver.find_element(By.XPATH, '(//a[@class="PH qG"])[1]')
        profile_click.click()
        sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей "Профиль"')
    def text_account():
        status_order_profile_text = driver.find_element(By.XPATH, '//div[@class="_6K _6J"]').text
        expected_result_status_profile = 'Привет!'
        if status_order_profile_text == expected_result_status_profile:
            print('Профиль - Текст совпал')
        else:
            print('Профиль - Текст не совпал')
        driver.back()
        sleep(3)

    click_account()
    text_account()


@allure.title('Бонусная карта')
def test_bonus_card(driver):
    @allure.step('Клик по Бонусная карта')
    def click_bonus_card():
        bonus_card_click = driver.find_element(By.XPATH, '(//a[@class="PH qN qG"])[1]')
        bonus_card_click.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Профиль"')
    def text_bonus_card():
        bonus_card_text = driver.find_element(By.XPATH, '//div[@class="t396__elem tn-elem tn-elem__5201800701669649091017"]').text
        expected_result_bonus_card = 'С бонусной картой выгоднее'
        if bonus_card_text == expected_result_bonus_card:
            print('Бонусная карта - Текст совпал')
        else:
            print('Бонусная карта - Текст не совпал')
        driver.back()

    click_bonus_card()
    text_bonus_card()


@allure.title('Корзина')
def test_open_cart(driver):
    @allure.step('Клик по кнопке Корзина')
    def click_cart():
        cart_click = driver.find_element(By.XPATH, '(//a[@class="PH qL qG"])[1]')
        cart_click.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Корзина"')
    def text_cart():
        cart_click_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_cart = 'Корзина'
        if cart_click_text == expected_result_cart:
            print('Корзина - Текст совпал')
        else:
            print('Корзина - Текст не совпал')
        driver.back()

    click_cart()
    text_cart()


@allure.title('Поле Поиск и ввод запроса')
def test_search(driver, action):
    @allure.step('Клик в поле Поиск и ввод данных в поле ввода')
    def click_search():
        search_click = driver.find_element(By.XPATH, '//li[@class="f_5 f_0"]')
        action.click(search_click).pause(2).send_keys('Hipp').pause(2).send_keys(Keys.ENTER).pause(2).perform()

    @allure.step('Сравнить текст открытой страницы со страницей результатов поиска')
    def text_search():
        search_result = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        search_result_test = search_result[0:20]
        expected_result_search = 'Нашлось по запросу: '
        if search_result_test == expected_result_search:
            print('Поиск - Текст совпал')
        else:
            print('Поиск - Текст не совпал')
        driver.back()

    click_search()
    text_search()


@allure.title('Клик по баннеру в поле меню')
def test_banner_menu(driver):
    @allure.step('Клик по баннеру в поле меню')
    def click_banner_menu():
        discount_menu = driver.find_element(By.XPATH, '//li[@class="f_5 f_9"]')
        discount_menu.click()

    @allure.step('Сравнить текст открытой страницы со страницей баннера')
    def text_banner():
        discount_menu_text = driver.find_element(By.XPATH, '//h1[@class="JM"]').text
        expected_result_discount = 'Ночь распродаж до -90%'
        if discount_menu_text == expected_result_discount:
            print('Баннер - Текст совпал')
        else:
            print('Баннер - Текст не совпал')
        driver.back()

    click_banner_menu()
    text_banner()


@allure.title('Клик по кнопке Акции')
def test_stock_menu(driver):
    @allure.step('Клик по кнопке Акции')
    def click_stock():
        stock_menu = driver.find_element(By.XPATH, '(//li[@class="f_5 gd"])[1]')
        stock_menu.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Акции"')
    def text_stock():
        stock_menu_text = driver.find_element(By.XPATH, '//h1[@class="_7S"]').text
        expected_result_stock = 'Акции'
        if stock_menu_text == expected_result_stock:
            print('Акции - Текст совпал')
        else:
            print('Акции - Текст не совпал')
        driver.back()

    click_stock()
    text_stock()


@allure.title('Наведение курсора на Категории с подкатегориями')
def test_category(driver, action):
    @allure.step('Наведение курсора на категории')
    def move_cursor_category():
        category_menu = driver.find_elements(By.XPATH, '//span[@class="ge"]')
        for i in range(2, 9):
            action.move_to_element(category_menu[i]).pause(1).perform()

    @allure.step('Наведение курсора на Еще категории')
    def move_more_category():
        more_menu = driver.find_element(By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')
        action.move_to_element(more_menu).pause(1).perform()
        category_menu_2 = driver.find_elements(By.XPATH, '//span[@class="ge"]')
        action.move_to_element(more_menu).perform()
        for i in range(9, 19):
            action.move_to_element(category_menu_2[i]).pause(1).perform()

    move_cursor_category()
    move_more_category()


@allure.title('Одежда и обувь')
def test_clothes_and_shoes(driver):
    @allure.step('Клик по "Одежда и обувь"')
    def open_shoes():
        category_menu3 = driver.find_element(By.XPATH, '(//span[@class="ge"])[3]')
        category_menu3.click()
        sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей "Одежда и обувь"')
    def text_shoes():
        category_menu3_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu3 = 'Обувь, одежда и аксессуары'
        if category_menu3_text == expected_result_category_menu3:
            print('Одежда и обувь - Текст совпал')
        else:
            print('Одежда и обувь - Текст не совпал')
        driver.back()
        sleep(1)

    open_shoes()
    text_shoes()


@allure.title('Подгузники и гигиена')
def test_hygiene(driver):
    @allure.step('Клик по Подгузники и гигиена')
    def open_hygiene():
        category_menu4 = driver.find_element(By.XPATH, '(//a[@class="f_8"])[3]')
        category_menu4.click()
        sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей "Подгузники и гигиена"')
    def text_hygiene():
        category_menu4_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu4 = 'Гигиена и уход'
        if category_menu4_text == expected_result_category_menu4:
            print('Подгузники и гигиена - Текст совпал')
        else:
            print('Подгузники и гигиена - Текст не совпал')
        driver.back()
        sleep(1)
    open_hygiene()
    text_hygiene()


@allure.title('Питание и кормление')
def test_nutrition(driver):
    @allure.step('Клик по Питание и кормление')
    def open_nutrition():
        category_menu5 = driver.find_element(By.XPATH, '(//span[@class="ge"])[5]')
        category_menu5.click()
        sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей "Питание и кормление"')
    def text_nutrition():
        category_menu5_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu5 = 'Кормление для детей'
        if category_menu5_text == expected_result_category_menu5:
            print('Питание и кормление - Текст совпал')
        else:
            print('Питание и кормление - Текст не совпал')
        driver.back()
        sleep(1)

    open_nutrition()
    text_nutrition()


@allure.title('Игрушки и игры')
def test_toys(driver):
    @allure.step('Клик по Игрушки и игры')
    def open_toys():
        category_menu6 = driver.find_element(By.XPATH, '(//span[@class="ge"])[6]')
        category_menu6.click()
        sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей "Игрушки и игры"')
    def text_toys():
        category_menu6_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu6 = 'Игрушки для детей'
        if category_menu6_text == expected_result_category_menu6:
            print('Игрушки и игры - Текст совпал')
        else:
            print('Игрушки и игры - Текст не совпал')
        driver.back()
        sleep(1)

    open_toys()
    text_toys()


@allure.title('Детская комната')
def test_children_room(driver):
    @allure.step('Клик по Детская комната')
    def open_children_room():
        category_menu7 = driver.find_element(By.XPATH, '(//span[@class="ge"])[7]')
        category_menu7.click()
        sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей "Детская комната"')
    def text_children_room():
        category_menu7_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu7 = 'Детская комната'
        if category_menu7_text == expected_result_category_menu7:
            print('Детская комната - Текст совпал')
        else:
            print('Детская комната - Текст не совпал')
        driver.back()
        sleep(1)

    open_children_room()
    text_children_room()


@allure.title('Прогулки и путешествия')
def test_travel(driver):
    @allure.step('Клик по Прогулки и путешествия')
    def open_travels():
        category_menu8 = driver.find_element(By.XPATH, '(//span[@class="ge"])[8]')
        category_menu8.click()
        sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей "Прогулки и путешествия"')
    def text_travels():
        category_menu8_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu8 = 'Прогулки и путешествия'
        if category_menu8_text == expected_result_category_menu8:
            print('Прогулки и путешествия - Текст совпал')
        else:
            print('Прогулки и путешествия - Текст не совпал')
        driver.back()
        sleep(1)

    open_travels()
    text_travels()


@allure.title('Канцтовары и товары для школы')
def test_school_supplies(driver):
    @allure.step('Клик по Канцтовары и товары для школы')
    def open_school_supplies():
        category_menu9 = driver.find_element(By.XPATH, '(//span[@class="ge"])[9]')
        category_menu9.click()
        sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей "Канцтовары и товары для школы"')
    def text_school_supplies():
        category_menu9_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu9 = 'Товары для школы'
        if category_menu9_text == expected_result_category_menu9:
            print('Канцтовары и товары для школы - Текст совпал')
        else:
            print('Канцтовары и товары для школы - Текст не совпал')
        driver.back()
        sleep(1)

    open_school_supplies()
    text_school_supplies()


@allure.title('Спорт и отдых')
def test_school_supplies(driver, action):
    @allure.step('Наведение курсора на "Еще"')
    def move_cursor():
        more_menu = driver.find_element(By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')
        action.move_to_element(more_menu).perform()

    @allure.step('Клик по Спорт и отдых')
    def open_sport():
        category_menu10 = driver.find_element(By.XPATH, '(//span[@class="ge"])[10]')
        category_menu10.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Спорт и отдых"')
    def text_sport():
        category_menu10_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu10 = 'Детские товары для спорта и отдыха'
        if category_menu10_text == expected_result_category_menu10:
            print('Спорт и отдых - Текст совпал')
        else:
            print('Спорт и отдых - Текст не совпал')
        driver.back()
        sleep(1)

    move_cursor()
    open_sport()
    text_sport()


@allure.title('Хобби и творчество')
def test_hobby(driver, action):
    @allure.step('Наведение курсора на "Еще"')
    def move_cursor():
        more_menu = driver.find_element(By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')
        action.move_to_element(more_menu).perform()

    @allure.step('Клик по Хобби и творчество')
    def open_hobby():
        category_menu11 = driver.find_element(By.XPATH, '(//span[@class="ge"])[11]')
        category_menu11.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Хобби и творчество"')
    def text_hobby():
        category_menu11_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu11 = 'Товары для творчества'
        if category_menu11_text == expected_result_category_menu11:
            print('Хобби и творчество - Текст совпал')
        else:
            print('Хобби и творчество - Текст не совпал')
        driver.back()
        sleep(1)

    move_cursor()
    open_hobby()
    text_hobby()


@allure.title('Книги')
def test_books(driver, action):
    @allure.step('Наведение курсора на "Еще"')
    def move_cursor():
        more_menu = driver.find_element(By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')
        action.move_to_element(more_menu).perform()

    @allure.step('Клик по Книги')
    def open_books():
        category_menu12 = driver.find_element(By.XPATH, '(//span[@class="ge"])[12]')
        category_menu12.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Книги"')
    def text_books():
        category_menu12_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu12 = 'Книги для детей'
        if category_menu12_text == expected_result_category_menu12:
            print('Книги - Текст совпал')
        else:
            print('Книги - Текст не совпал')
        driver.back()
        sleep(1)

    move_cursor()
    open_books()
    text_books()


@allure.title('Продукты для здоровья и спорта')
def test_health_products(driver, action):
    @allure.step('Наведение курсора на "Еще"')
    def move_cursor():
        more_menu = driver.find_element(By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')
        action.move_to_element(more_menu).perform()

    @allure.step('Клик по Продукты для здоровья и спорта')
    def open_products():
        category_menu13 = driver.find_element(By.XPATH, '(//span[@class="ge"])[13]')
        category_menu13.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Продукты для здоровья и спорта"')
    def text_products():
        category_menu13_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu13 = 'Продукты для здоровья и спорта'
        if category_menu13_text == expected_result_category_menu13:
            print('Продукты для здоровья и спорта - Текст совпал')
        else:
            print('Продукты для здоровья и спорта - Текст не совпал')
        driver.back()
        sleep(1)

    move_cursor()
    open_products()
    text_products()


@allure.title('Дом')
def test_house(driver, action):
    @allure.step('Наведение курсора на "Еще"')
    def move_cursor():
        more_menu = driver.find_element(By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')
        action.move_to_element(more_menu).perform()

    @allure.step('Клик по Дом')
    def open_house():
        category_menu14= driver.find_element(By.XPATH, '(//span[@class="ge"])[14]')
        category_menu14.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Дом"')
    def text_house():
        category_menu14_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu14 = 'Дом'
        if category_menu14_text == expected_result_category_menu14:
            print('Дом - Текст совпал')
        else:
            print('Дом - Текст не совпал')
        driver.back()
        sleep(1)

    move_cursor()
    open_house()
    text_house()


@allure.title('Бытовая техника и электроника')
def test_electronics(driver, action):
    @allure.step('Наведение курсора на "Еще"')
    def move_cursor():
        more_menu = driver.find_element(By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')
        action.move_to_element(more_menu).perform()

    @allure.step('Клик по Бытовая техника и электроника')
    def open_electronics():
        category_menu15= driver.find_element(By.XPATH, '(//span[@class="ge"])[15]')
        category_menu15.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Бытовая техника и электроника"')
    def text_electronics():
        category_menu15_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu15 = 'Бытовая техника и электроника'
        if category_menu15_text == expected_result_category_menu15:
            print('Бытовая техника и электроника - Текст совпал')
        else:
            print('Бытовая техника и электроника - Текст не совпал')
        driver.back()
        sleep(1)

    move_cursor()
    open_electronics()
    text_electronics()


@allure.title('Для родителей')
def test_for_parents(driver, action):
    @allure.step('Наведение курсора на "Еще"')
    def move_cursor():
        more_menu = driver.find_element(By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')
        action.move_to_element(more_menu).perform()

    @allure.step('Клик по Для родителей')
    def open_for_parents():
        category_menu16= driver.find_element(By.XPATH, '(//span[@class="ge"])[16]')
        category_menu16.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Для родителей"')
    def text_for_parents():
        category_menu16_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu16 = 'Товары для родителей'
        if category_menu16_text == expected_result_category_menu16:
            print('Для родителей - Текст совпал')
        else:
            print('Для родителей - Текст не совпал')
        driver.back()
        sleep(1)

    move_cursor()
    open_for_parents()
    text_for_parents()


@allure.title('Товары для животных от Зоозавра')
def test_pet_products(driver, action):
    @allure.step('Наведение курсора на "Еще"')
    def move_cursor():
        more_menu = driver.find_element(By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')
        action.move_to_element(more_menu).perform()

    @allure.step('Клик по Товары для животных от Зоозавра')
    def open_pet_products():
        category_menu17 = driver.find_element(By.XPATH, '(//span[@class="ge"])[17]')
        category_menu17.click()

    @allure.step('Сравнение ссылки Зоозавр с открытой')
    def url_pet_products():
        zoo_url = driver.current_url
        zoo_url_parse = urlparse(zoo_url)
        zoo_url_scheme = zoo_url_parse.scheme
        zoo_url_netloc = zoo_url_parse.netloc
        base_url = f'{zoo_url_scheme}://{zoo_url_netloc}/'
        if base_url == 'https://zoozavr.ru/':
            print("Ссылка совпала")
        else:
            print("Ссылка не совпала")
        driver.back()
        sleep(5)

    move_cursor()
    open_pet_products()
    url_pet_products()


@allure.title('Подарки')
def test_gifts(driver, action, wd):
    @allure.step('Наведение курсора на "Еще"')
    def move_cursor():
        more_menu = wd.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')))
        action.move_to_element(more_menu).perform()
        sleep(2)

    @allure.step('Клик по Подарки')
    def open_gifts():
        category_menu18 = driver.find_element(By.XPATH, '(//a[@class="f_8"])[18]')
        category_menu18.click()

    @allure.step('Сравнить текст открытой страницы со страницей "Подарки"')
    def text_gifts():
        category_menu18_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu18 = 'Подарки для детей'
        if category_menu18_text == expected_result_category_menu18:
            print('Подарки - Текст совпал')
        else:
            print('Подарки - Текст не совпал')
        driver.back()
        sleep(1)

    move_cursor()
    open_gifts()
    text_gifts()


@allure.title('Промокоды')
def test_promo_codes(driver, action, wd):
    @allure.step('Наведение курсора на "Еще"')
    def move_cursor():
        more_menu = wd.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[1]/header/div[4]/nav/div/ul/li[21]/button')))
        action.move_to_element(more_menu).perform()
        sleep(2)

    @allure.step('Клик по Промокоды')
    def open_promo_codes():
        category_menu19 = driver.find_element(By.XPATH, '(//a[@class="f_8"])[19]')
        category_menu19.click()
        sleep(2)

    @allure.step('Сравнить текст открытой страницы со страницей "Промокоды"')
    def text_promo_codes():
        category_menu19_text = driver.find_element(By.XPATH, '//h1[@class="HG"]').text
        expected_result_category_menu19 = 'Промокоды'
        if category_menu19_text == expected_result_category_menu19:
            print('Промокоды - Текст совпал')
        else:
            print('Промокоды - Текст не совпал')
        driver.back()
        sleep(3)

    move_cursor()
    open_promo_codes()
    text_promo_codes()



