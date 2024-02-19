import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open()
    calculator_page.set_delay(45)
    calculator_page.click_number(7)
    calculator_page.click_operator('+')
    calculator_page.click_number(8)
    calculator_page.click_equals()

    result = calculator_page.get_result()
    expected_result = '15'
    assert result == expected_result
    print(f"Expected result: {expected_result}, Actual result: {result}")

