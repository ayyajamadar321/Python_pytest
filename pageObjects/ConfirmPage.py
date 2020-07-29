from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country_text = (By.XPATH, "//input[@id='country']")
    india_text = (By.XPATH, "//li//a[text()='India']")
    term_text = (By.XPATH, "//label[contains(text(),'I agree with the')]")
    purbutton_text = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    alert_text = (By.CLASS_NAME, "alert-success")

    def CountryItem(self):
        return self.driver.find_element(*ConfirmPage.country_text)

    def IndiaItem(self):
        return self.driver.find_element(*ConfirmPage.india_text)

    def TermItem(self):
        return self.driver.find_element(*ConfirmPage.term_text)

    def PurbuttonItem(self):
        return self.driver.find_element(*ConfirmPage.purbutton_text)

    def AlertItem(self):
        return self.driver.find_element(*ConfirmPage.alert_text)