from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def enter_value(self, value):
        input_field = self.driver.find_element(By.ID, "delay")
        input_field.clear()
        input_field.send_keys(value)

    def click_button(self, button_text):
        button = self.driver.find_element(By.xpath(f"//button[text()='{button_text}']"))
        button.click()

    def get_result(self):
        result_element = WebDriverWait(self.driver, 45).until(
            EC.visibility_of_element_located((By.ID, "display")))
        return result_element.text







class CalculatorActions:

    def __init__(self, driver):
        self.page = CalculatorPage(driver)

    def perform_calculation(self, value):
        self.page.enter_value(value)
        self.page.click_button('7')
        self.page.click_button('+')
        self.page.click_button('8')
        self.page.click_button('=')







import unittest
from selenium import webdriver
from calculator_page import CalculatorActions

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_calculator(self):
        calculator = CalculatorActions(self.driver)
        calculator.page.open_page("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        calculator.perform_calculation('45')

        result = calculator.page.get_result()
        self.assertEqual(result, '15')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()































