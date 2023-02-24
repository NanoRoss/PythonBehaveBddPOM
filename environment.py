from browser import Browser
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CheckoutPage import CheckoutPage
from pages.LoginPage import LoginPage

def before_all(context):
    context.browser = Browser()
    context.LoginPage = LoginPage()
    context.InventoryPage = InventoryPage()
    context.CheckoutPage = CheckoutPage()
    context.LoginPage = LoginPage()


def after_all(context):
    context.browser.close()
