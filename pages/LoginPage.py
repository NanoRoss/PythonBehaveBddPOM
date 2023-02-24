from time import sleep
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#password')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login-button')

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        sleep(3)
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        sleep(2)
        self.driver.find_element(*self.LOGIN_BTN).click()
        sleep(2)

    def validateUserAreInLogin(self):
        try:
            self.driver.find_element(*self.LOGIN_BTN)
            return True
        except:
            return False



