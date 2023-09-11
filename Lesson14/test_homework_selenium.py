import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

sign_up_button = driver.find_element(By.XPATH, "//button[text() = 'Sign up']")
sign_up_button.click()

name_field = driver.find_element(By.ID, "signupName")
name_field.send_keys("John")

last_name_field = driver.find_element(By.ID, "signupLastName")
last_name_field.send_keys("Dou")

email_field = driver.find_element(By.ID, "signupEmail")
email_field.send_keys("johndo1110111@gmail.com")

password_field = driver.find_element(By.ID, "signupPassword")
password_field.send_keys("Qwerty12345")

repeat_password_field = driver.find_element(By.ID, "signupRepeatPassword")
repeat_password_field.send_keys("Qwerty12345")

register_button = driver.find_element(By.XPATH, "//button[text() = 'Register']")
register_button.click()

def test_check_registration():
    time.sleep(5)
    check_registration = driver.find_element(By.XPATH,
                                             "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/div/p")
    assert check_registration.text == "You don’t have any cars in your garage"
