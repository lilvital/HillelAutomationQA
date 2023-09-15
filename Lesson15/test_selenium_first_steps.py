import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from Lesson15.facade.registration_facade import RegistrationFacade



class TestBase:
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._session = requests.session()
        self._registration_facade = RegistrationFacade(self._driver)


        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    # def teardown_method(self):
    #
    #     print("PARENT")

class TestRegistration(TestBase):
    def setup_class(self):
        self.user_email = "hgjksasdasdaasdsdaasdasddads1fsdsadfd21123@test.com"
        self.user_password = "Qwerty1234"

        self.user_to_login = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

    def teardown_method(self):
        print("CHILD")
        self._session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user_to_login)
        self._session.delete(url="https://qauto2.forstudy.space/api/users")
        self._driver.quit()

    def test_registration_test(self):
        self._registration_facade.register_user("test", "testlastname", self.user_email, self.user_password, self.user_password)
        assert self._registration_facade.check_is_user_logged_in()


    def test_registration_1_test(self):
        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        sign_up_button = self._driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_button.click()
        name_field = self._driver.find_element(By.ID, "signupName")
        name_field.send_keys("test")
        last_name_field = self._driver.find_element(By.ID, "signupLastName")
        last_name_field.send_keys("lastnametest")
        email_field = self._driver.find_element(By.ID, "signupEmail")
        email_field.send_keys(self.user_email)
        password_field = self._driver.find_element(By.ID, "signupPassword")
        password_field.send_keys(self.user_password)
        repeat_password_field = self._driver.find_element(By.ID, "signupRepeatPassword")
        repeat_password_field.send_keys(self.user_password)
        register_button = self._driver.find_element(By.XPATH, '//button[text()="Register"]')
        register_button.click()
        empty_garage = self._driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")
        assert len(empty_garage) != 0