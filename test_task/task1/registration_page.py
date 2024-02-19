from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from time import sleep


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    def fill_form(self, first_name, last_name, address, email, phone, zip_code, city, country, job_position, company):
        self.driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys(company)

    def get_element_by_class(self, class_name):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        return element

    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()
