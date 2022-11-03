from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\PYTHON PROJEKTY\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Test")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Testowy")

email = driver.find_element(By.NAME, "email")
email.send_keys("test@testowy.com")

sign_up = driver.find_element(By.CLASS_NAME, "btn-primary")
sign_up.click()

driver.quit()
