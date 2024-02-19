import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from im import LoginPage, CartPage, CheckoutPage, SummaryPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping_flow(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    cart_page = CartPage(driver)
    cart_page.add_items_to_cart()
    cart_page.open_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_shipping_info("Юлия", "Мелихова", "399770")

    summary_page = SummaryPage(driver)
    actual_total = summary_page.get_total_amount()
    expected_total = "$58.29"
    actual_value = actual_total.split(":")[1].strip()
    comparison_result = f"Expected total: {expected_total}, Actual total: {actual_value}"
    print(comparison_result)
    assert actual_value == expected_total, f"Expected total {expected_total}, but got {actual_value}"
