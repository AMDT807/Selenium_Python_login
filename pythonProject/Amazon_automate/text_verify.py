from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# import time
driver.maximize_window()
driver.get("https://www.amazon.in/")

driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]/span/span').click()

# logo = driver.find_element(By.CSS_SELECTOR, '#a-page > div.a-section.a-padding-medium.auth-workflow > div.a-section.a-spacing-none.auth-navbar > div > a > i.a-icon.a-icon-logo')
# print("test", logo)
# if logo.text == '':
#     print("Logo not visible")
# else:
#     print("logo is visible")


# Sign in text verify
content = driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]')
if content.text != 'Sign in':
    print('Text is wrong')
else:
    print('Text is Correct')

forgot = driver.find_element(By.CLASS_NAME, 'a-form-label')
print("test", forgot.text)
if forgot.text == 'Email or mobile phone number':
    print('Text is correct')
else:
    print('Text is wrong')

    passwd = driver.find_element(By.XPATH, '//a[@id="auth-fpp-link-bottom"]').text
    if passwd == 'Forgot Password':
        print("Text of link is correct")
    else:
        print("Text of link is incoorect")


while True:
    pass
