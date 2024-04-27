import json
from selenium.webdriver.common.by import By
from time import sleep
import undetected_chromedriver as webdriver
import undetected_chromedriver as uc
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def browser():
    driver = uc.Chrome()
    driver.get("https://xn--e1aar9b.xn--e1aaa0add1ai6f.xn--p1ai/")
    driver.maximize_window()

    element = driver.find_element(By.CLASS_NAME, "catalog-sections-horizontal")
    links = element.find_elements(By.TAG_NAME, "a")

    for link in links:
        href = link.get_attribute("href")
        print(href)

    print(len(links))
    baby_menu(driver)


def baby_menu(driver):
    """We go to the children's menu and write down the name and price in the list."""
    driver.execute_script("window.scrollBy(0, 400);")
    sleep(5)
    baby_menu_click = driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div/div[2]/div/div[2]/div[1]/a[2]')
    baby_menu_click.click()
    sleep(5)

    baby_menu_link = driver.find_element(By.CLASS_NAME, 'catalog-items--grid')
    baby_menu_link_items = baby_menu_link.find_elements(By.TAG_NAME, "a")

    unique_links = set()

    for link in baby_menu_link_items:
        href = link.get_attribute('href')
        if href != "javascript:void(0);":
            unique_links.add(href)

    for link in unique_links:
        print(link)

    print(len(unique_links))

    items = driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div/div[2]/div/div[2]/div[4]/div')
    spans = items.find_elements(By.TAG_NAME, 'span')

    txt_spans = []

    for i in range(3, len(spans), 4):
        txt_span = spans[i].text
        txt_spans.append(txt_span)
        json_spans = json.dumps(txt_spans)

    print(txt_spans)

    baby_menu_txt = ""
    for i in range(0, len(txt_spans), 2):
        baby_menu_txt += f"{txt_spans[i]} - {txt_spans[i + 1]}\n"
    print(baby_menu_txt)


browser()
