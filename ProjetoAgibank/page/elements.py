import time
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class ElementsPage:
    def __init__(self):
        self.driver = conftest.driver

    def inscrever_newsletter(self, email):
        self.driver.find_element(By.XPATH, "//input[@id='subscribe-field']").send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@name='jetpack_subscriptions_widget']").click()
        iframe = self.driver.find_element(By.XPATH, "//iframe[@id='memberships-modal-iframe']")
        self.driver.switch_to.frame(iframe)

    def access_post(self):
        self.driver.find_element(By.XPATH, "//article[@class='uagb-post__inner-wrap']/h3[@class='uagb-post__title uagb-post__text']/a[@href='https://blogdoagi.com.br/cartao-virtual/']").click()

    def search_field(self, search):
        self.driver.find_element(By.XPATH, "//*[@class='slide-search astra-search-icon']").click()
        self.driver.find_element(By.XPATH, "//*[@id='search-field']").send_keys(search, Keys.ENTER)