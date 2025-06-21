import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")  # Firefox supports this flag
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    yield driver
    driver.quit()
