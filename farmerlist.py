from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

APP_PACKAGE = "com.mpower.android.app.lpin.crm"
APP_ACTIVITY = "com.mpower.android.lpincrm.views.activities.FarmerListActivity" 
 
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


farmer_profile = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '(//androidx.cardview.widget.CardView[@resource-id="com.mpower.android.app.lpin.crm:id/cvParentFarmerList"])[1]/android.widget.LinearLayout')
    )
).click()

farmer_profile_edit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Button[@text="EDIT"]')
    )
).click()

name_input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/etFarmerNameAddFarmer"]')
    )
)
name_input_field.clear()
name_input_field.send_keys("Motin Ali")

address_input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvAddressAddFarmer"]')
    )
)
address_input_field.clear()
address_input_field.send_keys("badda")

gender = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsGenderAddFarmer"]')
    )
).click()
gender_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="পুরুষ"]')
    )
).click()

picture = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvGalleryPickerAddFarmer"]/android.widget.ImageView')
    )
).click()
picture_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '(//android.widget.ImageView[@resource-id="android:id/icon"])[1]')
    )
).click()
picture_take = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '(//android.widget.TextView[@resource-id="com.miui.gallery:id/pick_num_indicator"])[10]')
    )
).click()

division = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsDivisionAddFarmer"]')
    )
).click()
division_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Chittagong"]')
    )
).click()

district = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsDistrictAddFarmer"]')
    )
).click()
district_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Chandpur"]')
    )
).click()

sub_district = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsUpazilaAddFarmer"]')
    )
).click()
sub_district_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Chandpur Sadar"]')
    )
).click()

union = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Spinner[@resource-id="com.mpower.android.app.lpin.crm:id/acsUnionAddFarmer"]')
    )
).click()
union_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Chandra"]')
    )
).click()


nid = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvNIDNOAddFarmer"]')
    )
).send_keys('4445551212')

driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
    '.scrollIntoView(new UiSelector().resourceId("com.mpower.android.app.lpin.crm:id/cvDatePickerAddFarmer"))'
)


# dob = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvDatePickerAddFarmer"]/android.widget.ImageView')
#     )
# ).click()

# clicks_needed = 25
# for i in range(clicks_needed):
#     next_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable(
#             (By.XPATH, '//android.widget.ImageButton[@content-desc="Previous month"]')
#         )
#     )
#     next_button.click()
#     print(f"Next button clicked {i + 1} time(s)")
#     time.sleep(1)
# dob_date = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.view.View[@content-desc="23 October 2022"]')
#     )
# ).click()
# dob_ok = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')
#     )
# ).click()


# image = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvGalleryPickerNIDAddFarmer"]/android.widget.ImageView')
#     )
# ).click()
# image_click = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '(//android.widget.ImageView[@resource-id="android:id/icon"])[1]')
#     )
# ).click()
# image_select = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '((//android.widget.TextView[@resource-id="com.miui.gallery:id/pick_num_indicator"])[11]')
#     )
# ).click()

submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/btnSubmitAddFarmer"]')
    )
).click()
