from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

APP_PACKAGE = "com.mpower.android.app.lpin.crm"
APP_ACTIVITY = "com.mpower.android.lpincrm.views.activities.DashboardActivity" 
 
# Define options for the Android device and application
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14.0"  # api level
options.device_name = "eoveidq4luoq8ifvw" # device id
options.app_package = APP_PACKAGE
options.app_activity = APP_ACTIVITY
options.no_reset = True  # Prevent resetting the app on each run
 
# Start the driver
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)

service_instant = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvTreatment"]/android.widget.LinearLayout')
    )
).click()

service_type = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[1]')
    )
).click()

sick = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="অসুস্থতার সেবা"]')
    )
).click()

farmer_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvNameTreatment"]')
    )
).send_keys('Rahim')

mobile_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvMobileTreatment"]')
    )
).send_keys('01945332212')

driver.quit()

address_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvAddressTreatment"]')
    )
).send_keys('nikunja')

animal = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[2]')
    )
).click()
animal_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="ছাগল"]')
    )
).click()

animal_type = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[3]')
    )
).click()
animal_type_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="খাসী"]')
    )
).click()

medicine = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.ImageButton[@resource-id="com.mpower.android.app.lpin.crm:id/fabMedicine"]')
    )
).click()
medicine_suggest = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsDisease"]')
    )
).click()
medicine_suggest_type = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="অপুষ্টি"]')
    )
).click()
medicine_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '(//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsMedicines"])[2]')
    )
).click()
medicine_name_type = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="Inj. Calcivit Plus"]')
    )
).click()
medicine_schedule = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/acivSubmitDialog"]')
    )
).click()
medicine_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitMedicine"]')
    )
).click()

driver.quit()