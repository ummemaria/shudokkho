from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the app package and activity
APP_PACKAGE = "com.mpower.android.app.lpin.crm"
APP_ACTIVITY = "com.mpower.android.lpincrm.views.activities.CalculationActivity"      # com.mpower.android.app.lpin.crm/com.mpower.android.lpincrm.views.activities.CalculationActivity

# Define options for the Android device and application
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14.0"  # Replace with your device's API level
options.device_name = "eoveidq4luoq8ifvw"  # Replace with your device ID
options.app_package = APP_PACKAGE
options.app_activity = APP_ACTIVITY
options.no_reset = True  # Prevent resetting the app on each run

# Start the driver
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)

# try:
#     print("App started successfully at the DashboardActivity!")
#     # Add actions to interact with elements on this page if needed

# except Exception as e:
#     print(f"Error occurred: {e}")

# finally:
#     # Quit the driver

due = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Button[@text="বাকির তালিকা"]')
    )
).click()

driver.quit()
