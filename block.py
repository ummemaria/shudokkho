from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APP_PACKAGE = "com.mpower.android.app.lpin.crm"
APP_ACTIVITY = "com.mpower.android.lpincrm.views.activities.DashboardActivity"

# Define options for the Android device and application
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14.0"  # API level
options.device_name = "eoveidq4luoq8ifvw"  # Device ID
options.app_package = APP_PACKAGE
options.app_activity = APP_ACTIVITY
options.no_reset = True  # Prevent resetting the app on each run

# Start the driver
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)

# try:
    # Service instant click
service_instant = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvTreatment"]/android.widget.LinearLayout')
        )
    ).click()

    # Select service type
service_type = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '(//android.widget.TextView[@resource-id="android:id/text1"])[1]')
        )
    ).click()

    # Select "অসুস্থতার সেবা"
sick = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="অসুস্থতার সেবা"]')
        )
    ).click()

    # Input farmer name
farmer_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvNameTreatment"]')
        )
    ).send_keys('Rahim')

    # Input mobile number
mobile_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvMobileTreatment"]')
        )
    ).send_keys('01945332212')

    # Input address
address_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvAddressTreatment"]')
        )
    ).send_keys('Nikunja')

    # Select animal type
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

    # Select animal subtype
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

    # Medicine details
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

driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId("com.mpower.android.app.lpin.crm:id/mbSubmitMedicine"))'
)



medicine_submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitMedicine"]')
        )
    ).click()


# finally:
    # Quit the driver at the end
driver.quit()

