from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

sign_up_button = driver.find_element(By.XPATH, "//button[text() = 'Sign up']")
sign_up_button.click()

name_field = driver.find_element(By.ID, "signupName")
name_field.send_keys("John")

last_name_field = driver.find_element(By.ID, "signupLastName")
last_name_field.send_keys("Dou")

email_field = driver.find_element(By.ID, "signupEmail")
email_field.send_keys("johndou123@gmail.com")

password_field = driver.find_element(By.ID, "signupPassword")
password_field.send_keys("Qwerty12345")

repeat_password_field = driver.find_element(By.ID, "signupRepeatPassword")
repeat_password_field.send_keys("Qwerty12345")

register_button = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button")
register_button.click()

a = 0