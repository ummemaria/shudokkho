from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
 
# Define options for the Android device and application
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14.0"  # api level
options.device_name = "eoveidq4luoq8ifvw" # device id
options.app = "C:/Users/Umme Maria/Downloads/sudh/Shudokkho_QA_Debug_1.9.6.apk"  # Path to your APK
options.no_reset = True  # Optional, prevents resetting the app on each run
 
# Start the driver
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
# time.sleep(5)
# print("App launched successfully on Android Emulator!")
# try:
    # Locate the registration button using XPath and click it
    
tele_permission = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/actvPosCustomDialog"]')
    )
).click()

my_profile_back = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
    )
).click()

new_call_record = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvNewVisit"]/android.widget.LinearLayout')
    )
).click() 

farmer_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvFarmerNameNewVisit"]')
    )
).send_keys('Karim Mia')

mobile_number_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvMobileNewVisit"]')
    )
).send_keys('01730301311')

address_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvAddressNewVisit"]')
    )
).send_keys('Rampura')

clicks_needed = 3
for i in range(clicks_needed):
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/acivNextNewVisit"]')
        )
    )
    next_button.click()
    print(f"Next button clicked {i + 1} time(s)")
    time.sleep(1)  # Add delay to handle animations or slow responses


# next_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/acivNextNewVisit"]')
#     )
# ).click()

hour_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="2"]')
    )
).click()

driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("3"))'
)


hour_selection = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="3"]')
    )
).click()

# min_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etMinutesNextVisit"]')
#     )
# ).click()



# Locate the minute input field
minute_input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etMinutesNextVisit"]')
    )
)

# Clear the input field
minute_input_field.clear()
# print("Minute input field cleared successfully!")

# Input the value "30"
minute_input_field.send_keys("30")
# print("Value '30' entered into the minute input field!")

time_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="PM"]')
    )
).click()
time_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="PM"]')
    )
).click()

confirm = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitNewVisit"]')
    )
).click()






