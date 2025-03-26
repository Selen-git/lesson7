#1:

import unittest
from selenium import webdriver
from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage

class TestShop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def test_purchase_flow(self):
        login_page = LoginPage(self.driver)
        login_page.inputUsername("your_username") 
        login_page.inputPassword("your_password")
        login_page.clickLoginButton()

        main_page = MainPage(self.driver)
        main_page.addToCart("item_name")
        main_page.goToCart()

        cart_page = CartPage(self.driver)
        cart_page.clickCheckoutButton()
        expected_items = ["item_name"]
        cart_page.verifyCartContent(expected_items)

        checkout_page = CheckoutPage(self.driver)
        checkout_page.input_first_name("Oleg")
        checkout_page.input_last_name("Silkin")
        checkout_page.input_postal_code("12345")
        checkout_page.click_continue()

        total_amount = checkout_page.get_total_amount()
        self.assertEqual(total_amount, "$29.99", "Total amount does not match")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()









#2:

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDraverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login_as_standart_user(self):
        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.send_keys("standart_user")

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()



class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        add_to_cart_button = self.driver.find_element(By.XPATH, f"//div[@class='inventory_item_name'][text()='{product_name}']/following-sibling::button")
        add_to_cart_button.click()

    def checkout(self):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()



import unittest
from selenium import webdriver
from MainPage import MainPage
from CartPage import CartPage

class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.main_page = Main_page(self.driver)
        self.cart_page = Cart_page(self.driver)

    def test_shopping_cart(self):
        self.main_page.open()
        self.main_page.login_as_standart_user()

        products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]

        for product in products:
            self.cart_page.add_to_cart(product)

        self.cart_page.checkout()

        total_price = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        self.assertEqual(total_price, "$58.29")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()













  
