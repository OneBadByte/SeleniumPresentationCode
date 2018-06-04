import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys




class tools:
    driver = webdriver.Firefox()

    def goto_page(self, url):
        """I go to urls"""
        time.sleep(1)
        self.driver.get(url)

    def press_key(self, key):
        """"""
        time.sleep(1)
        ActionChains(self.driver).send_keys(key).perform()

    def click_on(self, css_selector):
        time.sleep(1)
        self.driver.find_element_by_css_selector(css_selector).click()

    def clear_and_enter_text(self, css_selector, text):
        time.sleep(1)
        self.click_on(css_selector)
        self.driver.find_element_by_css_selector(css_selector).clear()
        time.sleep(1)
        self.driver.find_element_by_css_selector(css_selector).send_keys(text)

    def close_selenium(self):
        self.driver.close()