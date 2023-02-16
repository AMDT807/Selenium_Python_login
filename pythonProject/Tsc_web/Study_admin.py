# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# serv_obj=Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
# driver= webdriver.Chrome(service=serv_obj)
# import time
#
# driver.maximize_window()
# driver.get("https://radxup-colectiv-dev.azurewebsites.net")
# driver.find_element(By.ID, 'formBasicEmail').send_keys("vasim@yopmail.com")
# driver.find_element(By.XPATH, '//button[@type="submit"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div/div/div/div/div[1]/div/div[1]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="responsive-navbar-nav"]/div[2]/div/span/img').click()
# # Build Data Form
# driver.find_element(By.XPATH, '//span[normalize-space()="Form Management"]').click()
# driver.find_element(By.XPATH, '//button[@class="btn btn-primary mx-1 primary-button-bg float-end"]').click()
# while True:
#     pass