from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
from time import sleep


chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver: WebDriver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.detmir.ru/")
action = ActionChains(driver)
wd = WebDriverWait(driver, 5)

cookie = {
    'name': 'DM_CookieNotification',
    'value': '0'
}


def region_and_cookies():
    # Регион и куки
    geo_click = driver.find_element(By.XPATH, './/span[contains(text(), "Верно!")]')
    action.pause(2).click(geo_click).perform()
    driver.add_cookie(cookie)
    driver.refresh()
    sleep(3)


def footer_click_1():
    # Баннер в шапке
    banner_footer = driver.find_element(By.XPATH, '//div[@class="rg fx"]')
    banner_footer.click()
    driver.back()

    # Клик по логотипу ЗООЗАВР
    zoo_click_fut = wd.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://zoozavr.ru"]')))
    zoo_click_fut.click()
    zoo_url = driver.current_url
    zoo_url_parse = urlparse(zoo_url)
    zoo_url_scheme = zoo_url_parse.scheme
    zoo_url_netloc = zoo_url_parse.netloc
    base_url = f'{zoo_url_scheme}://{zoo_url_netloc}/'
    if base_url == 'https://zoozavr.ru/':
        print("URL matched")
    else:
        print("URL not matched")
    driver.back()
    sleep(2)

    # Выбор региона
    choice_region_click = wd.until(EC.element_to_be_clickable((By.XPATH, '//li[@class="tv tO tE tH tw gc tC"]')))
    choice_region_click.click()
    sleep(2)
    info_name_region = driver.find_element(By.XPATH, '//h2[@class="pE Fu"]').text
    print(info_name_region)
    expected_result_region = 'Выбор региона'
    if info_name_region == expected_result_region:
        print('The page region corresponds to')
    else:
        print('The page region does not match')
    action.send_keys(Keys.ESCAPE).perform()

    # Выбор магазина
    shops_click = wd.until(EC.element_to_be_clickable((By.XPATH, '(//a[@class="s_8"])[1]')))
    action.pause(3).move_to_element(shops_click).click(shops_click).perform()
    info_name_shops = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    info_name_shops_str = info_name_shops[0:24]
    expected_result_shops = 'Магазины «Детский мир»: '
    if info_name_shops_str == expected_result_shops:
        print('The page shops corresponds to')
    else:
        print('The page shops does not match')
    driver.back()
    sleep(2)

    # Доставка и оплата
    delivery_click = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="tz"])[2]')))
    delivery_click.click()
    delivery_click_info = driver.find_element(By.XPATH, '//span[@class="k_7"]').text
    delivery_click_info_text = delivery_click_info[0:24]
    expected_result_delivery = 'Доставка и оплата: '
    if delivery_click_info_text == expected_result_delivery:
        print('The page delivery corresponds to')
    else:
        print('The page delivery does not match')
    driver.back()
    sleep(5)

    # Продавать в Детском мире
    sell_click = wd.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-container"]/div[1]/header/div[2]/div/div[1]/ul/li[4]/a')))
    sell_click.click()
    sell_click_info = wd.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="t396__elem tn-elem tn-elem__4854365141661933876993"]'))).text
    expected_result_sell = 'Продавайте на маркетплейсе\nДетского мира'
    if sell_click_info == expected_result_sell:
        print('The page sell corresponds to')
    else:
        print('The page sell does not match')
    driver.back()
    sleep(2)

    # Клик по кнопке Еще и Обмен и возврат товара
    more_click = wd.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="r_2"]')))
    action.click(more_click).pause(2).perform()
    exchange_click = wd.until(EC.element_to_be_clickable((By.XPATH, '(//li[@class="tv tO tH tw ge gf s_7"])[1]')))
    exchange_click.click()
    exchange_click_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_exchange = 'Обмен и возврат товара'
    if exchange_click_text == expected_result_exchange:
        print('The page exchange corresponds to')
    else:
        print('The page exchange does not match')
    driver.back()

    # Клик по кнопке Еще и Обратная связь
    more_click = wd.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="r_2"]')))
    action.click(more_click).pause(2).perform()
    feedback_click = driver.find_element(By.XPATH, '(//li[@class="tv tO tH tw ge gf s_7"])[2]')
    feedback_click.click()
    feedback_click_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_feedback = 'Обратная связь'
    if feedback_click_text == expected_result_feedback:
        print('The page feedback corresponds to')
    else:
        print('The page feedback does not match')
    driver.back()


def status_order():
    # Статус заказа
    status_order_click = driver.find_element(By.XPATH, '//div[@class="gp"]')
    status_order_click.click()
    status_order_click_text = driver.find_element(By.XPATH, '//h3[@class="_9t _9v baE bau baz"]').text
    expected_result_status_orders = 'Войдите или создайте профиль'
    if status_order_click_text == expected_result_status_orders:
        print('The page status order corresponds to')
    else:
        print('The page status order does not match')
    action.send_keys(Keys.ESCAPE).perform()
    sleep(2)
    status_order_profile_text = driver.find_element(By.XPATH, '//div[@class="_1z _1y"]').text
    expected_result_status_profile = 'Привет!'
    if status_order_profile_text == expected_result_status_profile:
        print('The page status profile corresponds to')
    else:
        print('The page status profile does not match')
    driver.back()
    action.send_keys(Keys.ESCAPE).perform()
    driver.back()


def chat():
    # Чат
    chat_click = driver.find_element(By.ID, 'button_ChatWidget')
    action.click(chat_click).pause(2).click(chat_click).pause(2).perform()
    driver.switch_to.frame(driver.find_element(By.ID, 'hde-iframe'))
    sleep(3)
    # Ввод имени в чат
    name_input = driver.find_element(By.XPATH, '//input[@placeholder="Имя"]')
    name_input.send_keys('Иван')
    # Ввод email в чат
    email_input = driver.find_element(By.XPATH, '//input[@placeholder="Э-почта"]')
    email_input.send_keys('ivan@ya.ru')
    # Ввод сообщения в чат
    message_input = driver.find_element(By.XPATH, '//textarea[@placeholder="Отправить ваш вопрос Ctrl+Enter"]')
    message_input.send_keys('Hello!')
    # Клик по чекбоксу
    check_chat_click = driver.find_element(By.XPATH, '//span[@class="el-checkbox__inner"]')
    check_chat_click.click()
    # Отправить сообщение
    send_message_chat = driver.find_element(By.XPATH, '//button[@class="el-button custom-button-color el-button--info el-button--small is-plain"]')
    send_message_chat.click()
    # Закрыть чат
    close_chat = driver.find_element(By.XPATH, '//*[@id="widget-app"]/div[1]/i')
    close_chat.click()
    print('The message has been sent')


def switching_iframe():
    # Переключение на другой iframe
    driver.switch_to.default_content()


def footer_click_2():
    # Клик по логотипу
    logo_click = driver.find_element(By.XPATH, '//a[@class="qZ q_"]')
    logo_click.click()

    # Клик по профилю
    profile_click = driver.find_element(By.XPATH, '(//i[@class="dZ d_3 rc"])[1]')
    profile_click.click()
    sleep(2)
    status_order_profile_text = driver.find_element(By.XPATH, '//div[@class="_1z _1y"]').text
    expected_result_status_profile = 'Привет!'
    if status_order_profile_text == expected_result_status_profile:
        print('The page status profile corresponds to')
    else:
        print('The page status profile does not match')
    driver.back()
    sleep(3)

    # Клик по Бонусной карте
    bonus_card_click = driver.find_element(By.XPATH, '(//a[@class="Qj rf q_8"])[1]')
    bonus_card_click.click()
    bonus_card_text = driver.find_element(By.XPATH, '//div[@class="t396__elem tn-elem tn-elem__5201800701669649091017"]').text
    expected_result_bonus_card = 'С бонусной картой выгоднее'
    if bonus_card_text == expected_result_bonus_card:
        print('The page bonus card corresponds to')
    else:
        print('The page bonus card does not match')
    driver.back()

    # Клик по Корзина
    cart_click = driver.find_element(By.XPATH, '(//a[@class="Qj rd q_8"])[1]')
    cart_click.click()
    cart_click_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_cart = 'Корзина'
    if cart_click_text == expected_result_cart:
        print('The page cart corresponds to')
    else:
        print('The page cart does not match')
    driver.back()


def category_menu_1():
    # Клик по полю Поиск и ввод запроса
    search_click = driver.find_element(By.XPATH, '//li[@class="gH gC"]')
    action.click(search_click).pause(2).send_keys('Hipp').pause(2).send_keys(Keys.ENTER).pause(2).perform()
    search_result = driver.find_element(By.XPATH, '//p[@class="if"]').text
    search_result_test = search_result[0:20]
    expected_result_search = 'Нашлось по запросу: '
    if search_result_test == expected_result_search:
        print('The page search corresponds to')
    else:
        print('The page search does not match')
    driver.back()

    # Клик по баннеру в поле меню
    discount_menu = driver.find_element(By.XPATH, '//li[@class="gH gL"]')
    discount_menu.click()
    discount_menu_text = driver.find_element(By.XPATH, '//h1[@class="HS"]').text
    expected_result_discount = 'КиберДни'
    if discount_menu_text == expected_result_discount:
        print('The page discount corresponds to')
    else:
        print('The page discount does not match')
    driver.back()


def category_menu_2():
    # Клик по кнопке Акции
    stock_menu = driver.find_element(By.XPATH, '(//li[@class="gH gP"])[1]')
    stock_menu.click()
    stock_menu_text = driver.find_element(By.XPATH, '//h1[@class="TX"]').text
    expected_result_stock = 'Акции'
    if stock_menu_text == expected_result_stock:
        print('The page stock corresponds to')
    else:
        print('The page stock does not match')
    driver.back()

    # Наведение курсора на Категории с подкатегориями
    category_menu = driver.find_elements(By.XPATH, '//span[@class="gQ"]')
    for i in range(3, 9):
        action.move_to_element(category_menu[i]).pause(1).perform()
    # Наведение курсора на Еще категории
    more_menu = driver.find_element(By.XPATH, '//li[@class="gH gI"]')
    # Наведение курсора на Категории с подкатегориями
    category_menu2 = driver.find_elements(By.XPATH, '//span[@class="gQ"]')
    action.move_to_element(more_menu).perform()
    for i in range(9, 17):
        action.move_to_element(category_menu2[i]).pause(1).perform()
    print('The cycles are completed')

    # Клик по Одежда и обувь
    category_menu3 = driver.find_element(By.XPATH, '(//span[@class="gQ"])[3]')
    category_menu3.click()
    sleep(2)
    category_menu3_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu3 = 'Обувь, одежда и аксессуары'
    if category_menu3_text == expected_result_category_menu3:
        print('The page menu3 corresponds to')
    else:
        print('The page menu3 does not match')
    driver.back()
    sleep(1)

    # Клик по Подгузники и гигиена
    category_menu4 = driver.find_element(By.XPATH, '(//span[@class="gQ"])[4]')
    category_menu4.click()
    sleep(2)
    category_menu4_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu4 = 'Гигиена и уход'
    if category_menu4_text == expected_result_category_menu4:
        print('The page menu4 corresponds to')
    else:
        print('The page menu4 does not match')
    driver.back()
    sleep(1)

    # Клик по Питание и кормление
    category_menu5 = driver.find_element(By.XPATH, '(//span[@class="gQ"])[5]')
    category_menu5.click()
    sleep(2)
    category_menu5_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu5 = 'Кормление для детей'
    if category_menu5_text == expected_result_category_menu5:
        print('The page menu5 corresponds to')
    else:
        print('The page menu5 does not match')
    driver.back()
    sleep(1)

    # Клик по Игрушки и игры
    category_menu6 = driver.find_element(By.XPATH, '(//span[@class="gQ"])[6]')
    category_menu6.click()
    sleep(2)
    category_menu6_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu6 = 'Игрушки для детей'
    if category_menu6_text == expected_result_category_menu6:
        print('The page menu6 corresponds to')
    else:
        print('The page menu6 does not match')
    driver.back()
    sleep(1)

    # Клик по Детская комната
    category_menu7 = driver.find_element(By.XPATH, '(//span[@class="gQ"])[7]')
    category_menu7.click()
    sleep(2)
    category_menu7_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu7 = 'Детская комната'
    if category_menu7_text == expected_result_category_menu7:
        print('The page menu7 corresponds to')
    else:
        print('The page menu7 does not match')
    driver.back()
    sleep(1)

    # Клик по Прогулки и путешествия
    category_menu8 = driver.find_element(By.XPATH, '(//span[@class="gQ"])[8]')
    category_menu8.click()
    sleep(2)
    category_menu8_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu8 = 'Прогулки и путешествия'
    if category_menu8_text == expected_result_category_menu8:
        print('The page menu8 corresponds to')
    else:
        print('The page menu8 does not match')
    driver.back()
    sleep(1)
    # Клик по Спорт и отдых
    category_menu9 = driver.find_element(By.XPATH, '(//span[@class="gQ"])[9]')
    category_menu9.click()
    sleep(2)
    category_menu9_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu9 = 'Детские товары для спорта и отдыха'
    if category_menu9_text == expected_result_category_menu9:
        print('The page menu9 corresponds to')
    else:
        print('The page menu9 does not match')
    driver.back()
    sleep(1)


def more_menu_move():
    more_menu = wd.until(EC.element_to_be_clickable((By.XPATH, '//li[@class="gH gI"]')))
    action.move_to_element(more_menu).perform()
    sleep(1)


def category_menu_3():
    more_menu_move()
    category_menu10 = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="gQ"])[10]')))
    category_menu10.click()
    category_menu10_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu10 = 'Товары для школы'
    if category_menu10_text == expected_result_category_menu10:
        print('The page menu10 corresponds to')
    else:
        print('The page menu10 does not match')
    driver.back()

    more_menu_move()
    category_menu11 = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="gQ"])[11]')))
    category_menu11.click()
    category_menu11_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu11 = 'Товары для творчества'
    if category_menu11_text == expected_result_category_menu11:
        print('The page menu11 corresponds to')
    else:
        print('The page menu11 does not match')
    driver.back()

    more_menu_move()
    category_menu12 = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="gQ"])[12]')))
    category_menu12.click()
    category_menu12_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu12 = 'Книги для детей'
    if category_menu12_text == expected_result_category_menu12:
        print('The page menu12 corresponds to')
    else:
        print('The page menu12 does not match')
    driver.back()

    more_menu_move()
    category_menu13 = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="gQ"])[13]')))
    category_menu13.click()
    category_menu13_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu13 = 'Продукты для здоровья и спорта'
    if category_menu13_text == expected_result_category_menu13:
        print('The page menu13 corresponds to')
    else:
        print('The page menu13 does not match')
    driver.back()

    more_menu_move()
    category_menu14 = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="gQ"])[14]')))
    category_menu14.click()
    category_menu14_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu14 = 'Дом'
    if category_menu14_text == expected_result_category_menu14:
        print('The page menu14 corresponds to')
    else:
        print('The page menu14 does not match')
    driver.back()

    more_menu_move()
    category_menu15 = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="gQ"])[15]')))
    category_menu15.click()
    category_menu15_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu15 = 'Бытовая техника и электроника'
    if category_menu15_text == expected_result_category_menu15:
        print('The page menu15 corresponds to')
    else:
        print('The page menu15 does not match')
    driver.back()

    more_menu_move()
    category_menu16 = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="gQ"])[16]')))
    category_menu16.click()
    category_menu16_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu16 = 'Товары для родителей'
    if category_menu16_text == expected_result_category_menu16:
        print('The page menu16 corresponds to')
    else:
        print('The page menu16 does not match')
    driver.back()

    more_menu_move()
    category_menu17 = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="gQ"])[17]')))
    category_menu17.click()
    zoo_url = driver.current_url
    zoo_url_parse = urlparse(zoo_url)
    zoo_url_scheme = zoo_url_parse.scheme
    zoo_url_netloc = zoo_url_parse.netloc
    base_url = f'{zoo_url_scheme}://{zoo_url_netloc}/'
    if base_url == 'https://zoozavr.ru/':
        print("URL matched menu17")
    else:
        print("URL not matched menu17")
    driver.back()
    sleep(3)

    try:
        close_window_stock = wd.until(EC.element_to_be_clickable((By.XPATH, '(//button[@class="close"])[1]')))
        if close_window_stock.is_displayed():
            close_window_stock.click()
    except NoSuchElementException:
        print("Close button not found")

    sleep(3)
    more_menu_move()
    category_menu18 = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="gQ"])[18]')))
    category_menu18.click()
    category_menu18_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu18 = 'Подарки для детей'
    if category_menu18_text == expected_result_category_menu18:
        print('The page menu18 corresponds to')
    else:
        print('The page menu18 does not match')
    driver.back()

    more_menu_move()
    category_menu19 = wd.until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="gQ"])[19]')))
    category_menu19.click()
    category_menu19_text = driver.find_element(By.XPATH, '//h1[@class="x_1"]').text
    expected_result_category_menu19 = 'Промокоды'
    if category_menu19_text == expected_result_category_menu19:
        print('The page menu19 corresponds to')
    else:
        print('The page menu19 does not match')
    driver.back()


def start():
    region_and_cookies()
    footer_click_1()
    status_order()
    chat()
    switching_iframe()
    footer_click_2()
    category_menu_1()
    category_menu_2()
    category_menu_3()


start()

