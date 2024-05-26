import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():

    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://blogdoagi.com.br/")

    yield

    driver.quit()
