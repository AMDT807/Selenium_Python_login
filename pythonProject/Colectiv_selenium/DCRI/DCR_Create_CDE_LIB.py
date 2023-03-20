from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
serv_obj = Service("C:\WebDriver\chromedriver_win32 (1)\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://radxup-colectiv-dev.azurewebsites.net/")
email_box = driver.find_element(By.ID, 'formBasicEmail')
print("Display Status of Email Field:", email_box.is_displayed())
print("Enabled Status of Email Field:", email_box.is_enabled())

driver.find_element(By.ID, 'formBasicEmail').send_keys("var17@duke.edu")
time.sleep(1)

submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
print("Display status of Submit button:", submit_button.is_displayed())
print("Enabled status of Submit button:", submit_button.is_enabled())
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(5)

# CDE Library Management
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div[1]/div[4]/a/div/span').click()
time.sleep(5)

# add new library
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[2]/button').click()
time.sleep(6)

# enter version name
driver.find_element(By.ID, 'formName').send_keys("CDE CODEBOOK FOR TEST")
time.sleep(1)
# enter version number
driver.find_element(By.ID, 'formVersion').send_keys("VER1.0")
time.sleep(2)

# section name
driver.find_element(By.ID, 'sectionName').send_keys('Section one')
time.sleep(3)

# add question button
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/'
                              'div/div[1]/div[2]/div/div/span').click()
time.sleep(2)

# variable name
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/'
                              'div[3]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input').send_keys("Name")
time.sleep(3)

# ADD RESPONSES
driver.find_element(By.ID, 'selectQuestion').send_keys("Radio Button")
# driver.find_element(By.ID, 'selectQuestion').send_keys("Multiple Choice")
# driver.find_element(By.ID, 'selectQuestion').send_keys("Dropdown")
# driver.find_element(By.ID, 'selectQuestion').send_keys("Text Box")
# driver.find_element(By.ID, 'selectQuestion').send_keys("Number")
# driver.find_element(By.ID, 'selectQuestion').send_keys("Date")
# driver.find_element(By.ID, 'selectQuestion').send_keys("DateTime")
# driver.find_element(By.ID, 'selectQuestion').send_keys("Time")
# driver.find_element(By.ID, 'selectQuestion').send_keys("Descriptive")
time.sleep(3)

# ADD 1ST ADULT QUESTION
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]'
                              '/div[1]/div[2]/div[2]/div/div[1]/div[1]/input').send_keys("What is your name")
time.sleep(2)

# ADD HINT 1ST ADULT QUESTION
hintscroll = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]'
                              '/div[1]/div[2]/div[2]/div/div[2]/input')
driver.execute_script("arguments[0].scrollIntoView();",hintscroll)
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]'
                              '/div[1]/div[2]/div[2]/div/div[2]/input').send_keys("Tell your name")
time.sleep(3)

# values
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]'
                              '/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/input').send_keys("01")
time.sleep(2)

# adding options 1
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]'
                              '/div[2]/div/div[3]/div[3]/div/table/tr[2]/td[1]/div/input').send_keys("Option 1")
time.sleep(2)

# adding option 1's value
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]'
                              '/div/div[3]/div[3]/div/table/tr[2]/td[2]/div/input').send_keys("10")
time.sleep(2)

# click on add choice button
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div'
                              '/div[3]/div[4]/div/span').click()
time.sleep(2 )

# adding option 2
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div'
                              '/div[3]/div[3]/div/table/tr[3]/td[1]/div/input').send_keys("option 2")
time.sleep(2)

# adding option 2nd value
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div'
                              '/div[3]/div[3]/div/table/tr[3]/td[2]/div/input').send_keys("11")
time.sleep(2)

scroll_add_choice = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div'
                                                  '[1]/div[2]/div[2]/div''/div[3]/div[4]/div/span')
driver.execute_script("arguments[0].scrollIntoView();",scroll_add_choice)
time.sleep(2)

# adding Pediatric question
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]'
                              '/div[2]/div/div[1]/div[1]/input').send_keys("What is your name")
time.sleep(3)

# adding hint's
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]'
                              '/div[2]/div/div[2]/input').send_keys("Tell us your name")
time.sleep(3)

# adding value
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]'
                              '/div[2]/div/div[3]/div[2]/div[2]/div/input').send_keys("1000")
time.sleep(2)

# adding pediatric 1's option
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]'
                              '/div[2]/div/div[3]/div[3]/div/table/tr[2]/td[1]/div/input').send_keys("Pediatric 1")
time.sleep(3)

# adding pediatric 1's option -value
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]'
                              '/div/div[3]/div[3]/div/table/tr[2]/td[2]/div/input').send_keys("1001")
time.sleep(3)

# add choice button
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]'
                              '/div[2]/div/div[3]/div[4]/div/img').click()
time.sleep(2)

#add pediatric 2's option
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]'
                              '/div/div[3]/div[3]/div/table/tr[3]/td[1]/div/input').send_keys("Pediatric 2")
time.sleep(2)

# adding pediatric 2's option-value
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]'
                              '/div/div[3]/div[3]/div/table/tr[3]/td[2]/div/input').send_keys("112")
time.sleep(2)

# scroll div
ped = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]'
                              '/div/div[3]/div[3]/div/table/tr[3]/td[2]/div/input')
driver.execute_script("arguments[0].scrollIntoView();",ped)

# preview
driver.find_element(By.NAME, 'Preview').click()

# DIV OPEN FOR CDE PREVIEW
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[2]/img').click()

# save as draft
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div/button[2]').click()

# back
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div/button[1]').click()

# publish
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div/button[3]').click()

while True:
    pass