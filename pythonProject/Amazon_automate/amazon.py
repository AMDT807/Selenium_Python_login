from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver= webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://www.amazon.in/")

# login
print(driver.title)
# print(driver.current_url)
# print(driver.page_source)
driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]/span/span').click()
time.sleep(2)
email = driver.find_element(By.ID, 'ap_email')
print("Display Status of Email Field:", email.is_displayed())

print("Display Status of Email Field:", email.is_enabled())
driver.find_element(By.ID, 'ap_email').send_keys('7830767416')
time.sleep(2)
driver.find_element(By.ID, 'continue').click()
time.sleep(2)

# password
pwd=driver.find_element(By.ID, 'ap_password')
print("Displays Status of Password Field:", pwd.is_displayed())
print("Displays Status of Password Field:", pwd.is_enabled())
driver.find_element(By.ID, 'ap_password').send_keys('Amazon@123')
time.sleep(2)
submit=driver.find_element(By.ID, 'signInSubmit')
print("Display Status of submit button:", submit.is_displayed())
print("Display Status of submit button:", submit.is_enabled())

driver.find_element(By.ID, 'signInSubmit').click()
time.sleep(2)

# logo verify
# logo = driver.find_element(By.XPATH, '//*[@id="nav-logo-sprites"]')
# if logo.text == '':
#     print('Logo is not visible')
# else:
#     print('Logo is visible')

# language dropdown
driver.find_element(By.XPATH, '//*[@id="icp-nav-flyout"]/span/span[2]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="icp-language-settings"]/div[3]/div/label/i').click()
driver.find_element(By.XPATH, '//*[@id="icp-language-settings"]/div[2]/div/label/i').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="icp-save-button"]/span/input').click()

# #manage profile

# #object of ActionChains
# a = ActionChains(driver)
# #identify element
# m=driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]/span/span')
# #hover over element
# time.sleep(6)
# a.move_to_element(m).perform()
# driver.close()

# search item driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Apple Macbook Pro') driver.find_element(
# By.ID, 'nav-search-submit-button').click() driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[
# 1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').click() time.sleep(2) 1. scroll down
# by Pixel driver.execute_script("window.scrollBy(0,1000)","") 2 . scroll down page till element visible element=
# driver.find_element(By.ID, '') driver.execute_script("argument[0].scrollIntoView();",element) 3. scroll down till
# bottom driver.execute_script("window.scrollTo(1,document.body.scrollHeight)")

# add cart
# driver.find_element(By.ID, 'submit.add-to-cart').click()
# driver.find_element(By.ID, 'buy-now-button').click()

# perform all in amazon button
# driver.find_element(By.XPATH, '//*[@id="nav-hamburger-menu"]/span').click()
# time.sleep(2)



# Nab bar
# . 1 click amazon tv
time.sleep(10)
Verify_amazon_tv = driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[3]')
print(Verify_amazon_tv.text)
if Verify_amazon_tv.text == '':
    print('amazon tv is not clickable in nav bar')
else:
    print('amazon tv is visible on nav bar')
driver.find_element(By.LINK_TEXT, 'Amazon miniTV').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div['
                              '1]/div/div/div[1]/div[2]/div/img').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div/div[1]/div/div[2]/button/span').click()
time.sleep(10)
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]').click()
# driver.find_element(By.XPATH, '//img[@alt="settings"]').click()
# driver.find_element(By.XPATH, '//div[contains(text(),"Delete your miniTV data")]').click()
# driver.find_element(By.XPATH, '//button[normalize-space()="Yes, I want to"]').click()



#  2 Fresh
driver.find_element(By.LINK_TEXT, 'Fresh').click()
# 3 Grocery & Gourmet Foods
driver.find_element(By.LINK_TEXT, 'Grocery & Gourmet Foods').click()
# 4 Gift Ideas
driver.find_element(By.LINK_TEXT, 'Gift Ideas').click()
# 5 Best Sellers
driver.find_element(By.LINK_TEXT, 'Best Sellers').click()
while True:
    pass
