from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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

# e-ICF
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div[1]/div[3]/a/div/span').click()
time.sleep(3)

# Build New e_ICf
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[2]/button').click()
time.sleep(3)

# Select eicf type
select_eicf = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/select')
select_eicf.send_keys("Adult e-ICF ")
time.sleep(3)
# actions = ActionChains(driver)
# actions.move_to_element(select_eicf).click().perform()
# n=driver.find_element(By.CSS_SELECTOR, 'option[value="Adult"]')
# actions.move_to_element(n).click().perform()

# add eicf button
add_eicf = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
add_eicf.click()
time.sleep(4)
# Eicf Details
eicf_name = driver.find_element(By.ID, 'formName')
eicf_name.send_keys("E-icf Form for Above 18 years Old")
time.sleep(3)

eicf_form_version = driver.find_element(By.ID, 'formVersion')
eicf_form_version.send_keys("Version 1")
time.sleep(6)
driver.execute_script("window.scrollBy(0,500)", "")
time.sleep(2)

# description = driver.find_element(By.CLASS_NAME, 'mce-content-body ')
# description.send_keys("Welcome to the world of Radxup , we are here to help you ")

email_temp = driver.find_element(By.NAME, 'emailTemplate')
email_temp.send_keys("Survey Template")
time.sleep(4)
driver.execute_script("window.scrollBy(0,500)", "")
time.sleep(4)

add_question = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/div/'
											 'div/span').click()
time.sleep(3)
driver.execute_script("window.scrollBy(0,300)", "")

select_question_type = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[4]/div/div/div'
													 '[1]/div/div[2]/div/select').send_keys("Custom Question")
# select_question_type.send_keys("Custom Question")
time.sleep(1)












while True:
	pass
