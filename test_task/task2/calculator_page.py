from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_number(self, number):
        elements_with_number = self.driver.find_elements(By.XPATH, f"//*[contains(text(), '{number}')]")
        for element in elements_with_number:
            element.click()

    def click_operator(self, operator):
        elements_with_operator = self.driver.find_elements(By.XPATH, f"//*[contains(text(), '{operator}')]")
        for element in elements_with_operator:
            element.click()

    def click_equals(self):
        elements_with_equals = self.driver.find_elements(By.XPATH, "//*[contains(text(), '=')]")
        for element in elements_with_equals:
            element.click()

    def get_result(self):
        wait = WebDriverWait(self.driver, 50)
        result_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '15')]")))
        return result_element.text.split()[-1]