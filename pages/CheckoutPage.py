from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class CheckoutPage(BasePage):
    CHECKOUT_BTN = (By.XPATH, '//button[@id="checkout"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#first-name')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#last-name')
    ZIP_CODE_INPUT = (By.CSS_SELECTOR, '#postal-code')
    CONTINUE_BTN = (By.CSS_SELECTOR, '#continue')
    FINISH_BTN = (By.XPATH, '//button[@id="finish"]')
    ASSERT_TEXT = (By.CSS_SELECTOR, 'h2[class="complete-header"]')


    def goToCheckout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()
        sleep(5)

    def completeCheckoutAndOverview(self):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys("MARIANO AUTOMATION")
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys("PANELLA")
        self.driver.find_element(*self.ZIP_CODE_INPUT).send_keys("2000")
        self.driver.find_element(*self.CONTINUE_BTN).click()
        self.driver.find_element(*self.FINISH_BTN).click()
        sleep(5)

    def validateSuccessfulPurchase(self):
        sleep(5)
        try:
            BasePage.isURLContainingText(self, "complete")
            return True
        except:
            return False


