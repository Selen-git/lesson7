import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestShop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_shopping_flow(self):
        self.driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(self.driver)
        login_page.login_as_standart_user()

        products_page = ProductPage(self.driver)
        products_page.add_to_cart("Sauce Labs Backpack")
        products_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        products_page.add_to_cart("Sauce Labs Onesie")

        products_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_out_form("John", "Doe", "12345")
        total_price = checkout_page.get_total_price()
        self.assertEqual(total_price, "$58.29")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
  





from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password)
        self.login_button = (By.ID, "login-button")

    def login_as_standart_user(self):
        self.driver.find_element(*self.username_input).send_keys("standart_user")
        self.driver.find_element(*self.password_input).send_keys("secret_sauce")
        self.driver.find_element(*self.login_button).click()




from selenium.webdriver.common.by import By

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_buttons = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
        self.cart_button = (By.ID, "shopping_cart_container")

    def add_to_cart(self, product_name):
        self.driver.find_element(By.XPATH, "//div[text()='{}']/following-sibling::div/button".format(product_name)).click()
      
    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()




from selenium.webdriver.common.by import By

class CartPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//a[@class='btn_action checkout_button']")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()




from selenium.webdriver.common.by import By

class CheckoutPage:

    def__init__(self, driver):
    self.driver = driver
    self.first_name_input (By.ID, "first-name")
    self.last_name_input (By.ID, "last-name")
    self.postal_code_input (By.ID, "postal_code")
    self.continue_button = (By.XPATH, "input[@type='submit']")
    self.total_label = (By.XPATH, "//div[@class='summary_subtotal_label']")

    def fill_out_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self):
        return self.driver.find_element(*self.total_label).text
        























