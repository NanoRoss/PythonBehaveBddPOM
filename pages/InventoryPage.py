from time import sleep
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_BTN = (By.XPATH, '(//button[contains(@class, "btn_inventory")])[{}]')
    GO_TO_CART_BTN = (By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    BURGER_MENU_BTN = (By.CSS_SELECTOR, '#react-burger-menu-btn')
    LOGOUT_MENU_BTN = (By.CSS_SELECTOR, '#logout_sidebar_link')

    def addToCartByID(self, index: int):
        xpath = self.ADD_TO_CART_BTN[1].format(index)
        add_to_cart_btn = self.driver.find_element(By.XPATH, xpath)
        add_to_cart_btn.click()
        sleep(5)

    def goToCart(self):
        self.driver.find_element(*self.GO_TO_CART_BTN).click()
        sleep(5)

    def openBurgerMenu(self):
        self.driver.find_element(*self.BURGER_MENU_BTN).click()
        sleep(5)

    def clickLogOut(self):
        self.driver.find_element(*self.LOGOUT_MENU_BTN).click()
        sleep(5)


