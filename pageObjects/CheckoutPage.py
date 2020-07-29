from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    mob_text = (By.CSS_SELECTOR, 'h4.card-title')
    add_text = (By.XPATH, "//*[@class='col-lg-3 col-md-6 mb-3'][4]//button")
    checkout_text = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    product_txt = (By.XPATH, "//th[text()='Product']")
    button_text = (By.XPATH, "//button[@class='btn btn-success']")

    def MobItems(self):
        return self.driver.find_elements(*CheckoutPage.mob_text)

    def AddItem(self):
        return self.driver.find_element(*CheckoutPage.add_text)

    def CheckItem(self):
        return self.driver.find_element(*CheckoutPage.checkout_text)

    def ProdItem(self):
        return self.driver.find_element(*CheckoutPage.product_txt)

    def ButtonItem(self):
        self.driver.find_element(*CheckoutPage.button_text).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
