import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browserName = request.config.getoption("browserName")

    if browserName == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browserName == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browserName == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
    else:
        print("No browser is selected so pass the correct browser name:" + browserName)
        raise Exception("Driver is not found")

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    print(driver.title)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
