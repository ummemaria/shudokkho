from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
# Define options for the Android device and application
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14.0"  # api level
options.device_name = "eoveidq4luoq8ifvw" # device id
options.app = "C:/Users/Umme Maria/Downloads/sudh/Shudokkho_QA_Debug_1.9.6.apk"  # Path to your APK
options.no_reset = True  # Optional, prevents resetting the app on each run
 
# Start the driver
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
time.sleep(5)
# print("App launched successfully on Android Emulator!")
# try:
    # Locate the registration button using XPath and click it
registration_button = driver.find_element("xpath", '//android.widget.Button[@text="নতুন একাউন্ট তৈরি করুন"]')
registration_button.click()
name_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etNameReg"]')
    )
).send_keys('Rime Tester')    

mobile_number_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etMobileReg"]')
    )
).send_keys('01952200190')

occupation = driver.find_element("xpath", '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsServiceType"]').click()
occupation = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="পল্লী প্রাণী সেবাকর্মী"]'))).click()

gender = driver.find_element("xpath", '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsGender"]').click()
gender = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="মহিলা"]'))).click()

age = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsAge"]')
    )
).click()
# time.sleep(3)
age = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="২৫-৩০ বছর"]')
    )
).click()

division = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsDivision"]')
    )
).click()
division = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Chittagong"]')
    )
).click()

district = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsDistrict"]')
    )
).click()
district = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Chandpur"]')
    )
).click()

sub_district = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsUpazila"]')
    )
).click()
sub_district = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Chandpur Sadar"]')
    )
).click()

union = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsUnion"]')
    )
).click()
union = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Chandra"]')
    )
).click()

experience = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsExperience"]')
    )
).click()
experience = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="৩ বছরের কম"]')
    )
).click()

# image = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/cvCameraPicker"]')
#     )
# ).click()
# camera_on = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.ImageView[@content-desc="Shutter"]')
#     )
# ).click()
# camera_click = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.ImageButton[@content-desc="Done"]')
#     )
# ).click()
# terms = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/info"]')
#     )
# ).click()
# okay = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/actvPosCustomDialog"]')
#     )
# ).click()

driver.find_element(
AppiumBy.ANDROID_UIAUTOMATOR,
'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.mpower.android.app.lpin.crm:id/mbSubmitReg"))')

submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitReg"]')
    )
).click()
submit_yes = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/actvPosCustomDialog"]')
    )
).click()

# otp_input = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etSMSCode"]')
#     )
# ).send_keys('9776')

# otp_code = input("Enter the OTP received: ")

#     # Locate the OTP input field and enter the OTP
# otp_field = driver.find_element("id", "com.mpower.android.app.lpin.crm:id/etSMSCode")  # Replace with actual ID
# otp_field.send_keys(otp_code)
# # submit = driver.find_element("xpath", '//android.widget.Button[@text="নিশ্চিত করুন"]').click()

# submit_done = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.Button[@text="নিশ্চিত করুন"]')
#     )
# ).click()




 
# finally:
#     # Close the driver
driver.quit()
    
 

