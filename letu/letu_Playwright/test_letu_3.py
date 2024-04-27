import re
from playwright.sync_api import Page, expect
from time import sleep


def test_example(context) -> None:
    page: Page = context.new_page()
    page.goto("https://www.letu.ru/")
    page.set_viewport_size({"width": 1650, "height": 1200})
    sleep(5)
    button_3(page)


def button_3(page: Page):
    for p in range(7):
        page.keyboard.press("ArrowDown")
    page.get_by_role("link", name="Letoile").click()
    page.get_by_role("button", name="L'Etoile").click()
    sleep(2)
    for p in range(7):
        page.keyboard.press("ArrowDown")
    page.get_by_role("link", name="DG").click()
    page.get_by_role("button", name="L'Etoile").click()
    sleep(2)
    for p in range(7):
        page.keyboard.press("ArrowDown")
    page.get_by_role("link", name="CLB").click()
    page.get_by_role("button", name="L'Etoile").click()
    sleep(2)
    for p in range(7):
        page.keyboard.press("ArrowDown")
    page.get_by_role("link", name="NARS").first.click()
    page.get_by_role("button", name="L'Etoile").click()
    sleep(2)
    for p in range(7):
        page.keyboard.press("ArrowDown")
    page.get_by_role("link", name="Antonio Maretti", exact=True).click()
    page.get_by_role("button", name="L'Etoile").click()
    sleep(2)
    for p in range(7):
        page.keyboard.press("ArrowDown")
    page.get_by_role("link", name="Lanvin").click()
    page.get_by_role("button", name="L'Etoile").click()
    sleep(2)
    for p in range(7):
        page.keyboard.press("ArrowDown")
    page.get_by_role("link", name="Trussardi").click()
    page.get_by_role("button", name="L'Etoile").click()
    sleep(2)
    for p in range(7):
        page.keyboard.press("ArrowDown")
    try:
        page.get_by_role("link", name="Pen").click()
        page.get_by_role("button", name="L'Etoile").click()
    except:
        for p in range(7):
            page.keyboard.press("ArrowDown")
        page.get_by_role("button", name="Все бренды").click()
        page.get_by_role("button", name="L'Etoile").click()
    print('<<<<<The test is passed!>>>>>')
