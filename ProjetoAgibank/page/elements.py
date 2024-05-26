import time
import conftest
from selenium.webdriver.common.by import By

class ElementsPage:
    def __init__(self):
        self.driver = conftest.driver

    def inscrever_newsletter(self, email):
        self.driver.find_element(By.XPATH, "//input[@id='subscribe-field']").send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@name='jetpack_subscriptions_widget']").click()

