from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://radxup-colectiv-dev.azurewebsites.net/")
email_box = driver.find_element(By.ID, 'formBasicEmail')
print("Display Status of Email Field:", email_box.is_displayed())
print("Enabled Status of Email Field:", email_box.is_enabled())

# Enter Credentials
driver.find_element(By.ID, 'formBasicEmail').send_keys("vasim@yopmail.com")
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

#Participant Management
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div[1]/div[5]/a/div/span").click()
time.sleep(3)

# Click Add Participant
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div/button').click()
time.sleep(8)


# Enter Email ID
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div/div[2]'
                                  '/div/div/input').send_keys("Jackkk@yopmail.com")
time.sleep(10)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div/div[2]/div/div/span/img').click()
time.sleep(3)

# First Name
driver.find_element(By.NAME, 'first_name').send_keys("Jackson")
time.sleep(2)
# Last Name
driver.find_element(By.NAME, 'last_name').send_keys("Edword")
time.sleep(2)
# Participant ID
driver.find_element(By.NAME, 'participant_id').send_keys("J1938")
time.sleep(2)

# Select Form
driver.find_element(By.NAME, 'form_code').send_keys("HIV DATA FORM")
time.sleep(3)

# Send Like Now
# driver.find_element(By.ID, 'formBasicCheckbox1').click()

# Don't Send Link
# driver.find_element(By.ID, 'formBasicCheckbox2').click()

# Click Add
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()

while True:
    pass