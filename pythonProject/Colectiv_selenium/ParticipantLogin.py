from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://radxup-colectiv-uat.azurewebsites.net/participant-login")
driver.find_element(By.CLASS_NAME, 'participant-signin').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button').click()
time.sleep(2)
driver.find_element(By.ID, 'formBasicEmail').send_keys("jhon@yopmail.com")
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys("Test@123!!")
time.sleep(2)
# login button
driver.find_element(By.CSS_SELECTOR, 'button').click()
time.sleep(1)
# passError = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div')
# if passError:
#     print('Password or email is not correct!')
#     driver.close()
# else:
#     print('Login Successfully')
# select study card

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div/div/div/div/div[1]/div/div[1]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="responsive-navbar-nav"]/div[2]/div/span/img').click()
time.sleep(2)
# perform web browser scrollable
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="responsive-navbar-nav"]/div[2]/div/span/img').click()

# Verify Study name
heading = driver.find_element(By.XPATH, '//*[@id="responsive-navbar-nav"]/div[1]/div[1]/span')
print("test", heading.text)
if heading.text == '':
    print('Study Name is not visible')
else:
    print('Study Name is visible')
time.sleep(2)

# Profile Dropdown
driver.find_element(By.XPATH, '//*[@id="dropdown-basic"]/img').click()
time.sleep(2)
# click setting on profile
driver.find_element(By.XPATH, '//*[@id="responsive-navbar-nav"]/div[2]/div/div[2]/div/div/a[2]').click()
time.sleep(2)

# profile dropdown- logout
# driver.find_element(By.XPATH, '//*[@id="responsive-navbar-nav"]/div[2]/div/div[2]/div/div/a[3]/img').click()


# click on profile button
# driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div/div[1]/div/div[2]/img').click()
# time.sleep(2)
# perform add mobile number
# driver.find_element(By.NAME, 'mobile_phone').send_keys("78656766758")
# time.sleep(2)
# perform update profile
# driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div/div[2]/div[3]/button').click()
# time.sleep(2)
#  profile update complete

# Update Password icon
# driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/img').click()
# time.sleep(3)
# driver.find_element(By.ID, 'formBasicPassword').send_keys("Test@123")
# time.sleep(3)
# driver.find_element(By.NAME, 'password').send_keys("Test@123!!")
# time.sleep(3)
# driver.find_element(By.NAME, 'confirmPassword').send_keys("Test@123!!")
# time.sleep(3)
# # Update pass_button
# driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/div/div/div[3]/div[3]/button').click()
# time.sleep(4)

while True:
    pass
