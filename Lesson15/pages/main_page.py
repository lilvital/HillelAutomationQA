from selenium.webdriver.common.by import By

from Lesson15.pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.sing_up_button = lambda: self._driver.find_element(By.XPATH, "//button[text()='Sign up']")