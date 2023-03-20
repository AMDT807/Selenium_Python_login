from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("http://13.126.253.245:9002/")

# verify Title of application
get_title = driver.title
print(get_title)

# Testing Email and Password
# time.sleep(2)
# case 1 - Enter valid Login Credentials
enter_email = driver.find_element(By.NAME, 'email')
enter_email.send_keys("mayank.negi@techsuperiors.com")
# time.sleep(2)
enter_pass = driver.find_element(By.NAME, 'password')
enter_pass.send_keys("Test@!!!!123")
# time.sleep(2)

# SignIN
signIn = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div/div[2]'
									   '/div/div[2]/div/div/div[4]/button')
signIn.click()
# time.sleep(5)

# Logout
driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/''div[2]/div[2]/div/div/span').click()
# time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]').click()
driver.quit()
#Case 2 - Enter Wrong Credentials


while True:
	pass