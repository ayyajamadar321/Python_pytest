import time
from pageObjects.HomePage import HomePage
from utilities.base import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItem()
        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        log.info("Getting all the cart Iteams")
        #checkoutPage = CheckoutPage(self.driver)
        ele_mobtext = checkoutPage.MobItems()
        #ele_mobtext = self.driver.find_elements(By.CSS_SELECTOR, 'h4.card-title')

        ele_add = checkoutPage.AddItem()
        #ele_add = self.driver.find_element(By.XPATH, "//*[@class='col-lg-3 col-md-6 mb-3'][4]//button")

        for ele in ele_mobtext:
            if ele.text == "Blackberry":
                time.sleep(1)
                ele_add.click()


        # ele_check = checkoutPage.CheckItem()
        checkoutPage.CheckItem().click()
        #ele_check = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Checkout')
        # time.sleep(2)
        # ele_check.click()

        # Product page  ****************************************************************
        ele_prod = checkoutPage.ProdItem()
        #ele_prod = self.driver.find_element(By.XPATH, "//th[text()='Product']")
        print(ele_prod.text)
        assert "Product" == ele_prod.text
        assert ele_prod.is_displayed()
        time.sleep(1)

        confirmPage = checkoutPage.ButtonItem()
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        log.info("Entering country name India")
        #confirmPage = ConfirmPage(self.driver)
        confirmPage.CountryItem().send_keys("INDIA")
        #self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("INDIA")

        self.verifyLinkPrasence("India")        #Explicite wait from base class

        confirmPage.IndiaItem().click()
        #self.driver.find_element(By.XPATH, "//li//a[text()='India']").click()

        confirmPage.TermItem().click()
        #self.driver.find_element(By.XPATH, "//label[contains(text(),'I agree with the')]").click()
        time .sleep(2)
        confirmPage.PurbuttonItem().click()
        #self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()

        ele_disp = confirmPage.AlertItem()
        #ele_disp = self.driver.find_element(By.CLASS_NAME, "alert-success")
        ans = ele_disp.text
        assert ele_disp.is_displayed()
        assert "Success!" in ans

        self.driver.get_screenshot_as_file("screen.png")