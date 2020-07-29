import pytest
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.base import BaseClass
import time


class TestHomepage(BaseClass):

    def test_formSubmition(self, getdata):
        homePage = HomePage(self.driver)
        homePage.nameItem().send_keys(getdata["firstname"])
        homePage.emailItem().send_keys(getdata["email"])
        homePage.passItem().send_keys(getdata["password"])
        homePage.checkboxItem()
        self.selectOptipn(homePage.genderItem(), getdata["gender"])
        homePage.radioItem()
        homePage.buttonItem()
        time.sleep(1)
        ans_ele = homePage.successItem().is_displayed()
        print(ans_ele)
        self.driver.get_screenshot_as_file("kity.png")
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_Homepage_Data)
    def getdata(self, request):
        return request.param
