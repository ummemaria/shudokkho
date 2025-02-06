from parent import ParentService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NewCallRecord(ParentService):
    def __init__(self, app_package, app_activity, platform_version, device_name):
        super().__init__(app_package, app_activity, platform_version, device_name)

    def perform_action(self):
        """Override the parent class method to perform specific actions related to New Call Record."""
        # Ensure driver is initialized
        if not self.driver:
            self.start_driver()

        try:
            # Example action: Granting permission
            tele_permission = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//android.widget.TextView[@resource-id="com.mpower.android.app.lpin.crm:id/actvPosCustomDialog"]')
                )
            ).click()

            # Starting a new call record
            new_call_record = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvNewVisit"]/android.widget.LinearLayout')
                )
            ).click()

            # Filling in details (Farmer, Mobile, Address)
            self.fill_farming_info()

            # Clicking "Next" button
            self.click_next_button(3)

            # Select time and confirm
            self.select_time_and_confirm()
            
        except Exception as e:
            print(f"Error during call record actions: {e}")
            self.close()
            raise

    def fill_farming_info(self):
        """Fill the farming information details."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvFarmerNameNewVisit"]')
            )
        ).send_keys('Karim Mia')

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvMobileNewVisit"]')
            )
        ).send_keys('01730301311')

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.mpower.android.app.lpin.crm:id/acactvAddressNewVisit"]')
            )
        ).send_keys('Rampura')

    def click_next_button(self, clicks_needed=3):
        """Click the 'Next' button multiple times."""
        for i in range(clicks_needed):
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/acivNextNewVisit"]')
                )
            )
            next_button.click()
            print(f"Next button clicked {i + 1} time(s)")
            time.sleep(1)

    def select_time_and_confirm(self):
        """Select the time and confirm the visit."""
        hour_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="2"]')
            )
        ).click()

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("3"))'
        )

        hour_selection = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="3"]')
            )
        ).click()

        minute_input_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etMinutesNextVisit"]')
            )
        )

        minute_input_field.clear()
        minute_input_field.send_keys("30")

        time_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="PM"]')
            )
        ).click()

        confirm = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitNewVisit"]')
            )
        ).click()
        print("Visit confirmed successfully.")
