from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import undetected_chromedriver as uc
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


start = time.time()
driver = uc.Chrome()
driver.get("https://www.lady-maria.ru/")
action = ActionChains(driver)
time.sleep(10)


# Вход в личный кабинет
# def log_in_account():
#     account_open = driver.find_element(By.XPATH, '//a[@class="top_panel-client"]')
#     account_open.click()
#
#     click_email = driver.find_element(By.XPATH, '//input[@id="email"]')
#     click_password = driver.find_element(By.XPATH, '//input[@id="password"]')
#
#     action.click(click_email).send_keys("введите свою почту здесь").send_keys(Keys.ENTER).perform()
#     action.click(click_password).send_keys("введите свой пароль здесь").pause(1).perform()
#
#     driver.find_element(By.XPATH, '//button[@name="commit"]').click()
#     driver.find_element(By.XPATH, '//div[@class="cell-4 cell-6-md cell-12-s"]').click()


def title_equal_category():
    li_items = driver.find_elements(By.CSS_SELECTOR, 'li.layout_menu-item.menu-item.level-1')
    li_item = driver.find_element(By.CSS_SELECTOR, 'li.layout_menu-item.menu-item.level-1')

    li_1 = []
    li_2 = []

    for li in li_items:
        category_page = li.text
        li_1.append(category_page.title())

    for li in range(len(li_items)):
        li_items = driver.find_elements(By.CSS_SELECTOR, 'li.layout_menu-item.menu-item.level-1')
        li_items[li].click()
        name_category = driver.find_element(By.CSS_SELECTOR, 'h1.collection-title.page-title').text
        li_2.append(name_category.title())

    print(li_1)
    print(li_2)

    if li_1 == li_2:
        print('ok')
    else:
        print('no')

    for a, b in zip(li_1, li_2):
        if a == b:
            print(f'{a} = {b}')
        else:
            print('no!!!!!!!')


def social_button():
    ok_button_main_page = driver.find_element(By.XPATH, '//a[@title="ok"]')
    ok_button_main_page.click()
    driver.switch_to.window(driver.window_handles[1])
    ok = driver.title
    driver.get_screenshot_as_png()
    driver.save_screenshot('ok.png')
    print(ok)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    vk_button_main_page = driver.find_element(By.XPATH, '//a[@title="Vkontakte"]')
    vk_button_main_page.click()
    driver.switch_to.window(driver.window_handles[1])
    vk = driver.title
    driver.get_screenshot_as_png()
    driver.save_screenshot('vk.png')
    print(vk)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    you_button_main_page = driver.find_element(By.XPATH, '//a[@title="Youtube"]')
    you_button_main_page.click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    you = driver.title
    driver.save_screenshot('you.png')
    print(you)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    tg_button_main_page = driver.find_element(By.XPATH, '//a[@title="Telegram"]')
    tg_button_main_page.click()
    driver.switch_to.window(driver.window_handles[1])
    tg = driver.title
    driver.get_screenshot_as_png()
    driver.save_screenshot('tg.png')
    print(tg)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def start_test_lady():
    # log_in_account() # раскомментируйте, если используете модуль авторизации
    title_equal_category()
    social_button()


start_test_lady()
end = time.time() - start
print(end)





