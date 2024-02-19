import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_items_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def open_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_shipping_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        ).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()


class SummaryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total_amount(self):
        sum_total = self.driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']")
        return sum_total.text

