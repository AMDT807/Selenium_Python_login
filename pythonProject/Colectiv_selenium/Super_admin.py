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

driver.find_element(By.ID, 'formBasicEmail').send_keys("var17@duke.edu")
time.sleep(1)

submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
print("Display status of Submit button:", submit_button.is_displayed())
print("Enabled status of Submit button:", submit_button.is_enabled())
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(5)

dashboard = driver.find_element(By.XPATH, '//span[normalize-space()="Dashboard"]')
if dashboard:
    driver.find_element(By.LINK_TEXT, "Study Management").click()
else:
    driver.implicitly_wait(10)
time.sleep(10)
# indentation
arr = [0]
for i in arr:
    driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]').click()
    time.sleep(10)
    # Enter study Details
    driver.find_element(By.NAME, 'study_id').send_keys("StudyOFSURVEY1" + str(i))
    time.sleep(4)
    driver.find_element(By.NAME, 'name').send_keys("CHOLERA DISEASE SURVEY" + str(i))
    time.sleep(4)
    driver.find_element(By.NAME, 'awardee_org').send_keys("Mahatma Gandhi Hospital")
    time.sleep(4)
    driver.find_element(By.ID, 'selectQuestion').send_keys("RADx-UP NIH CDEs Version 0.5")
    # time.sleep(4)
    # driver.find_element(By.NAME, 'description').send_keys("Struggling with a disjointed combination of Windows Task "
    #                                                       "Scheduler, cron, application specific schedulers and other "
    #                                                       "tools to try and manage your production?  We help companies "
    #                                                       "achieve a cross-platform single pane scheduling framework to "
    #                                                        "achieve coordinated production.")
    time.sleep(4)
    driver.find_element(By.NAME, 'date_share').click()
    time.sleep(5)
    # driver.find_element(By.CLASS_NAME, 'form-check-input').click()  This click on yes for system generate dates/
    driver.find_element(By.NAME, 'enable_group').click()
    time.sleep(5)

    #continue
    driver.find_element(By.XPATH, '//button[normalize-space()="Next"]').click()
    time.sleep(6)
    # CDE TO COLLECT SECTION
    # section 1 location
    driver.find_element(By.XPATH, '//div[contains(@class,"row mt-5 mb-5")]//div//div[1]//div[1]//div[1]//div[1]//input[1]').click()
    time.sleep(4)
    # section 2 Sociodemographics
    Sociodemographics = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div['
                                                      '2]/div[1]/div[1]/div[1]/input')
    driver.execute_script("arguments[0].scrollIntoView();", Sociodemographics)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(3)
    # close div
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/img').click()
    time.sleep(2)
    # SECTION 3: Housing, Employment And Insurance
    driver.execute_script("window.scrollBy(0,500)", "")
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[1]/input').click()
    time.sleep(3)
    # close div
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[2]/img').click()
    time.sleep(2)
    # SECTION 4: Medical History
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[4]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[4]/div[1]/div[2]/img').click()
    time.sleep(2)
    #  SECTION 5: Health Status
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[5]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[5]/div[1]/div[2]/img').click()
    # SECTION 6: Vaccine Acceptance
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[6]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[6]/div[1]/div[2]/img').click()
    # SECTION 7: Testing
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[7]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[7]/div[1]/div[2]/img').click()
    # SECTION 8: Covid Test
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[8]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[8]/div[1]/div[2]/img').click()
    time.sleep(3)
    # SECTION 9: Symptoms
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[9]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[9]/div[1]/div[2]/img').click()
    time.sleep(3)
    # SECTION 10: Alcohol And Tobacco
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[10]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[10]/div[1]/div[2]/img').click()
    time.sleep(3)
    # SECTION 11: Identity
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[11]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(3)
    # ScrLl to bottom
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    #click Next
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/div[3]/button").click()
    time.sleep(5)

    # CDE TO SHARE SECTION
    # section 1 location
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/input').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/img').click()
    time.sleep(2)

    # #  section 2 sociodemographics
    # # div open
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/img').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(2)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/img').click()
    time.sleep(3)

    # SECTION 3: Housing, Employment And Insurance
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[2]/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[1]/div[1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/div[2]/img').click()
    time.sleep(3)

    # SECTION 4: Medical History
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[4]/div[1]/div[2]/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[4]/div[1]/div[1]/div[1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[4]/div[1]/div[2]/img').click()
    time.sleep(3)

    # SECTION 5: Health Status
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[5]/div[1]/div[2]/img').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[5]/div[1]/div[1]/div[1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[5]/div[1]/div[2]/img').click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,300)", "")
    time.sleep(2)

    # SECTION 6: Vaccine Acceptance
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[6]/div[1]/div[2]/img').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[6]/div[1]/div[1]/div[1]/input').click()
    time.sleep(3)
    #div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[6]/div[1]/div[2]/img').click()
    time.sleep(3)

    # SECTION 7: Testing
    # div open
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[7]/div[1]/div[2]/img').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[7]/div[1]/div[1]/div[1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[7]/div[1]/div[2]/img').click()
    time.sleep(3)

    # SECTION 8: Covid Test
    # div open
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[8]/div[1]/div[2]/img').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[8]/div[1]/div[1]/div[1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[8]/div[1]/div[2]/img').click()
    time.sleep(3)

    # SECTION 9: Symptoms
    # div open
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[9]/div[1]/div[2]/img').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[9]/div[1]/div[1]/div[1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[9]/div[1]/div[2]/img').click()
    time.sleep(3)

    # SECTION 10: Alcohol And Tobacco
    # div open
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[10]/div[1]/div[2]/img').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[10]/div[1]/div[1]/div[1]/input').click()
    time.sleep(3)
    # div close
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[10]/div[1]/div[2]/img').click()
    time.sleep(3)

    # SECTION 11: Identity div open driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[
    # 2]/div/div[2]/div[11]/div[1]/div[2]/img').click() time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[11]/div[1]/div[1]/div['
                                  '1]/input').click()
    time.sleep(3)

    # scroll to bottom
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)

    # click to next button
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[3]/div[3]/button').click()
    time.sleep(2)

    # adding user
    driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div['
                                  '1]/div[1]/input[1]').send_keys("mayank@yopmail.com")
    time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/form/div/img').click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/form/div[1]/img').click()
    # time.sleep(6)
    # driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div['
    #                               '1]/div[1]/input[1]').send_keys("mayank@yopmail.com")
    # time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/form/div/img').click()
    # time.sleep(3)
    # driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/form/div[2]/div/input').send_keys("gaurav@yopmail.com")
    # time.sleep(2)
    # click next
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/button').click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # update study card
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[2]/div[2]/div/div[6]/div[3]/button').click()
    time.sleep(3)
    #update or cancel
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()
    time.sleep(3)
    # cancel
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]').click()

#  This is the end of Study Creation flow , and we are crating CDE Library from Below codes

# CDE Library Management
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div[1]/div[4]/a/div/span').click()
# time.sleep(5)
#
# # add new library
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[2]/button').click()
# time.sleep(6)
#
# # enter version name
# driver.find_element(By.ID, 'formName').send_keys("CDE CODEBOOK FOR TEST")
# time.sleep(1)
# # enter version number
# driver.find_element(By.ID, 'formVersion').send_keys("VER1.0")
# time.sleep(2)
#
# # section name
# driver.find_element(By.ID, 'sectionName').send_keys('Section one')
# time.sleep(3)
#
# # add question 1
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div/div/img').click()
# time.sleep(3)
#
# # variable name 1 ENGLISH
# driver.find_element(By.ID, 'sectionHint').send_keys("Name")
# time.sleep(2)
# driver.find_element(By.ID, 'selectQuestion').send_keys("Radio Button")
# time.sleep(2)
#
# # Adult field level
# # question 1
# driver.find_element(By.NAME, 'FormsSections.0.FSQuestions.0.Adult.question').send_keys("What is your Name?")
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,100)", "")
# # hint question 1
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[2]/input').send_keys("Tell us abot your name")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,200)", "")
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/input').send_keys("01")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,100)", "")
# # enter options
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/table/tr[2]/td[1]/div/input').send_keys("Mayank")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,100)", "")
# #add values
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/table/tr[2]/td[2]/div/input').send_keys("02")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,200)", "")
# time.sleep(2)
# # click on add choice button
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[4]/div/img').click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,200)", "")
# # add option for second choice
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/table/tr[3]/td[1]/div/input').send_keys("Gaurav")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,200)", "")
# # add values for second option
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/table/tr[3]/td[2]/div/input').send_keys("02")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,200)", "")
# # div close
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/img').click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,100)", "")
# time.sleep(8)
#
# # Pediatric Field Level
# # pediatric question 1
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div/div[1]/div[1]/input').send_keys("What is your Name")
# time.sleep(2)
# # pediatric question Hint
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div/div[2]/input').send_keys("Tell us about your name")
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,100)", "")
# # add value
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/input').send_keys("03")
# time.sleep(2)
# # add options for pediatirc
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div/div[3]/div[3]/div/table/tr[2]/td[1]/div/input').send_keys("Abhishek")
# time.sleep(2)
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div/div[3]/div[3]/div/table/tr[2]/td[2]/div/input').send_keys("05")
# time.sleep(2)
# # click on add choice
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div/div[3]/div[4]/div/span').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div/div[3]/div[3]/div/table/tr[3]/td[1]/div/input').send_keys("amit")
# time.sleep(2)
# # add values
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div/div[3]/div[3]/div/table/tr[3]/td[2]/div/input').send_keys("06")





while True:
    pass
