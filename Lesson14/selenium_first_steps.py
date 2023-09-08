from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
sign_up_button = driver.find_element(By.XPATH, "//button[text() = 'Sign up']")
sign_up_button.click()
name_field = driver.find_element(By.ID, "signupName")
name_field.send_keys("test123")
a = 0