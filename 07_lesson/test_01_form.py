from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        self.first_name = (By.NAME, "first-name")
        self.last_name = (By.NAME, "last-name")
        self.address = (By.NAME, "address")
        self.email = (By.NAME, "email")
        self.phone = (By.NAME, "phone")
        self.zip_code = (By.NAME, "zip-code")
        self.city = (By.NAME, "city")
        self.country = (By.NAME, "country")
        self.job_position = (By.NAME, "job-title")
        self.company = (By.NAME, "company")
        self.submit_button = (By.XPATH, "//button[@type='submit']")

        self.field_error = (By.CLASS_NAME, "error")

    def open_page(self):
        self.driver.get(self.url)

    def fill_form(self, first_name, last_name, address, email, phone, city, country, job_position, company):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.address).send_keys(address)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.phone).send_keys(phone)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.country).send_keys(country)
        self.driver.find_element(*self.job_position).send_keys(job_position)
        self.driver.find_element(*self.company).send_keys(company)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

    def check_field_highlighted_red(self, field_name):
        element = self.driver.find_element(*field_name)
        return "error" in element.get_attribute("class")

    def check_field_highlighted_green(self, field_name):
        element = self.driver.find_element(*field_name)
        return "valid" in element.get_attribute("class")

driver = webdriver.Chrome()
form_page = FormPage(driver)
form_page.open_page()
form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
form_page.submit_form()

zip_code_highlighted_red = form_page.check_field_highlighted_red(form_page.zip.code)
assert zip_code_highlighted_red, "Zip code field is not highlighted red"

other_fields_highlighted_green = all([form_page.check_field_highlighted_green(field) for field in [form_page.first_name, form_page.last_name, form_page.address, form_page.email, form_page.phone, form_page.city, form_page.country, form_page.job_position, form_page.company]])
assert other_fields_highlighted_green, "One or more fields are not highlighted green"

driver.quit()



































