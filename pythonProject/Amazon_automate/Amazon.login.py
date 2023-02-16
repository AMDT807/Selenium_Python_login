from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)
import time
driver.maximize_window()
driver.get("https://www.amazon.in/")

# forgot password
# driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]/span/span').click()
# time.sleep(2)
# driver.find_element(By.ID, 'ap_email').send_keys('7830767416')
# time.sleep(2)
# driver.find_element(By.ID, 'continue').click()
# time.sleep(2)
# driver.find_element(By.LINK_TEXT, 'Forgot Password').click()
# driver.find_element(By.ID, 'ap_email').clear()
# driver.find_element(By.ID, 'ap_email').send_keys("7830767416")
# driver.find_element(By.ID, 'continue').click()


# # positive scenarios for login

# driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]/span/span').click()
# driver.find_element(By.ID, 'createAccountSubmit').click()
# Enter details
# driver.find_element(By.ID, 'ap_customer_name').send_keys("Amazon User")
# time.sleep(2)
# driver.find_element(By.ID, 'ap_phone_number').send_keys("7055673754")
# time.sleep(2)
# driver.find_element(By.ID, 'ap_email').send_keys("spraygod716@gpmail.com")
# time.sleep(2)
# driver.find_element(By.ID, "ap_password").send_keys("Amazon@12345")
# time.sleep(2)
# driver.find_element(By.ID, 'continue').click()
# time.sleep(2)


#


# Verify if a user will be able to login with a valid username and valid password.
# Verify the ‘Forgot Password' functionality.
# Verify the ‘Remember Me’ functionality.
# Verify the validation messages for invalid login.
# Verify if a user is able to login with a new password once the password has changed.
# Verify the timeout functionality of the login session.
# Use enter button after typing the correct username and password.
# Use tab to navigate from username textbox to password textbox and then to login button.
# Verify the validation for the maximum allowed incorrect login attempt.
# Verify the login using deactivated user.





while True:
    pass




