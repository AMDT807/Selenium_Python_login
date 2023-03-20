from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.action_chains import ActionChains

import time
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("C:\\Drivers\\chromedriver_win32(1)\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://radxup-colectiv-dev.azurewebsites.net/")
email_box = driver.find_element(By.ID, 'formBasicEmail')
print("Display Status of Email Field:", email_box.is_displayed())
print("Enabled Status of Email Field:", email_box.is_enabled())

# Enter Credentials
driver.find_element(By.ID, 'formBasicEmail').send_keys("fever@yopmail.com")
time.sleep(1)

submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
print("Display status of Submit button:", submit_button.is_displayed())
print("Enabled status of Submit button:", submit_button.is_enabled())

# Click Submit
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(5)

# Select Study Card
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/div/div/div/div[1]').click()
time.sleep(4)

# Home Screen
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, 'Form Management').click() # click on Form Management

driver.implicitly_wait(5)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/button').click()

# Use Variables from existing form
driver.implicitly_wait(5)
driver.find_element(By.ID, 'radio2').click()
time.sleep(1)
driver.find_element(By.NAME, 'formCode').send_keys("Viral fever V1.0")
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click() # Add Button

time.sleep(4)
# Fill Forms Details
driver.implicitly_wait(4)
driver.find_element(By.ID, 'formName').send_keys("Viral fever")
driver.find_element(By.ID, 'formVersion').send_keys("V1.0")
driver.find_element(By.ID, 'formEventName').send_keys("Testing Form Dependency")
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[2]/div[4]/div/textarea').send_keys("A fever is a temporary rise in "
			"body temperature. It's one part of an overall response from the body's immune system."
		    " A fever is usually caused by an infection. For most children and adults, a fever may be "
	        "uncomfortable")
time.sleep(3)
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(3)
# Dependency
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[3]/div[3]/div[1]/div[2]/img').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[3]/div[3]/div[2]/div[2]/div/img').click()
# select Form
driver.find_element(By.ID, 'selectQuestion').send_keys("")






# Participant Facing
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[3]/div[4]/div[2]/div[3]/div/div[2]/div[1]/input').click()
time.sleep(2)
# Select Email temp
driver.find_element(By.NAME, 'emailTemplate').send_keys("Survey Template")
time.sleep(2)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[4]/div/button[3]').click()

driver.implicitly_wait(3)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[5]/div/button[3]').click()

while True :
	pass