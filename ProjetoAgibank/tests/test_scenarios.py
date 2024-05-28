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
        thanks = driver.find_element(By.XPATH, "//*[contains(text(), 'Confirme sua assinatura')]")
        time.sleep(1)
        driver.get_screenshot_as_file('Thanks_' + date_time + '.png')
        assert thanks.is_displayed()

    @pytest.mark.accessnews
    def test_access_news(self):
        today = datetime.now()
        date_time = today.strftime("%m-%d-%Y_%H-%M-%S")
        driver = conftest.driver
        elementspage = ElementsPage()
        elementspage.access_post()
        time.sleep(1)
        driver.get_screenshot_as_file('AccessPost_' + date_time + '.png')
        post = driver.find_element(By.XPATH, "//span[contains(text(),'Cartão Virtual: o que é e como usar')]")
        assert post.is_displayed()

    @pytest.mark.searchfield
    def test_search_field(self):
        today = datetime.now()
        date_time = today.strftime("%m-%d-%Y_%H-%M-%S")
        driver = conftest.driver
        elementspage = ElementsPage()
        elementspage.search_field("Conta Corrente")
        time.sleep(2)
        driver.get_screenshot_as_file('SearchField_' + date_time + '.png')
        resultsearch = driver.find_element(By.XPATH, "//h1[@class='page-title ast-archive-title']")
        assert resultsearch.is_displayed()

    @pytest.mark.emailcancel
    def test_email_cancel(self):
        today = datetime.now()
        date_time = today.strftime("%m-%d-%Y_%H-%M-%S")
        driver = conftest.driver
        elementspage = ElementsPage()
        elementspage.email_cancel("lucasmenezes@outlook.com")
        error = driver.find_element(By.XPATH, "//*[contains(text(), 'Ops! Parece que a assinatura com este e-mail foi cancelada.')]")
        time.sleep(1)
        driver.get_screenshot_as_file('Error_' + date_time + '.png')
        assert error.is_displayed()
