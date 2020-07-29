from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop_text = (By.CSS_SELECTOR, "a[href*='shop']")
    name_text = (By.NAME, "name")
    email_text = (By.NAME, "email")
    pass_text = (By.CSS_SELECTOR, "input#exampleInputPassword1")
    checkbox_text = (By.CSS_SELECTOR, "input#exampleCheck1")
    gender_text = (By.ID, "exampleFormControlSelect1")
    radio_text = (By.ID, "inlineRadio1")
    button_text = (By.XPATH, "//input[@class='btn btn-success']")
    success_text = (By.XPATH, "//strong[contains(text(),'Success!')]")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop_text).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def nameItem(self):
        return self.driver.find_element(*HomePage.name_text)

    def emailItem(self):
        return self.driver.find_element(*HomePage.email_text)

    def passItem(self):
        return self.driver.find_element(*HomePage.pass_text)

    def checkboxItem(self):
        return self.driver.find_element(*HomePage.checkbox_text).click()

    def genderItem(self):
        return self.driver.find_element(*HomePage.gender_text)

    def radioItem(self):
        return self.driver.find_element(*HomePage.radio_text).click()

    def buttonItem(self):
        return self.driver.find_element(*HomePage.button_text).click()

    def successItem(self):
        return self.driver.find_element(*HomePage.success_text)