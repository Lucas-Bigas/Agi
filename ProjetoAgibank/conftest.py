import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():

    global driver
    driver = webdriver.chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("")

    yield

    driver.quit()
