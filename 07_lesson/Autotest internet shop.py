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













  
