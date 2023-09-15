import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()

def test_check_registration(setup):
    driver = setup

    sign_up_button = driver.find_element(By.XPATH, "//button[text() = 'Sign up']")
    sign_up_button.click()

    name_field = driver.find_element(By.ID, "signupName")
    name_field.send_keys("John")

    last_name_field = driver.find_element(By.ID, "signupLastName")
    last_name_field.send_keys("Dou")

    email_field = driver.find_element(By.ID, "signupEmail")
    email_field.send_keys("johndo111031112101@gmail.com")

    password_field = driver.find_element(By.ID, "signupPassword")
    password_field.send_keys("Qwerty12345")

    repeat_password_field = driver.find_element(By.ID, "signupRepeatPassword")
    repeat_password_field.send_keys("Qwerty12345")

    register_button = driver.find_element(By.XPATH, "//button[text() = 'Register']")
    register_button.click()

    time.sleep(5)

    check_registration = driver.find_element(By.XPATH, "//p[text() = 'You don’t have any cars in your garage']")
    assert check_registration.text == "You don’t have any cars in your garage"

def test_example_teardown(setup):
    pass
