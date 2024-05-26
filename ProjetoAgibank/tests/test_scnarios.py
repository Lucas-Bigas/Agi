import time

import pytest
import conftest
from selenium.webdriver.common.by import By
from page.elements import ElementsPage
from datetime import datetime

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.alltests
class TestScenarios:
    @pytest.mark.accesssite
    def test_access_site(self):
        today = datetime.now()
        date_time = today.strftime("%m-%d-%Y_%H-%M-%S")
        driver = conftest.driver
        text = driver.find_element(By.XPATH, "//*[contains(text(), 'Últimas do Blog do Agi')]")
        driver.get_screenshot_as_file('Access_Blog_' + date_time + '.png')
        assert text.is_displayed()

    @pytest.mark.newsletter
    def test_register_newsletter(self):
        today = datetime.now()
        date_time = today.strftime("%m-%d-%Y_%H-%M-%S")
        driver = conftest.driver
        elementspage = ElementsPage()
        elementspage.inscrever_newsletter("lucasmenezes@outlook.com")
        driver.get_screenshot_as_file('Email_Register_' + date_time + '.png')
        confirmacao = driver.find_element(By.ID, '#thank_you')
        time.sleep(1)
        driver.get_screenshot_as_file('Thanks_' + date_time + '.png')
        assert confirmacao == "Confirme sua assinatura"

    @pytest.mark.accessnews
    def test_access_news(self):
        today = datetime.now()
        date_time = today.strftime("%m-%d-%Y_%H-%M-%S")
        driver = conftest.driver

    @pytest.mark.searchfield
    def test_search_field(self):
        today = datetime.now()
        date_time = today.strftime("%m-%d-%Y_%H-%M-%S")
        driver = conftest.driver
