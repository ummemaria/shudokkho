from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Schedule:
    def __init__(self, app_package, app_activity, platform_version, device_name):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = platform_version
        options.device_name = device_name
        options.app_package = app_package
        options.app_activity = app_activity
        options.no_reset = True  # Ensures app data isn't reset

        self.driver = webdriver.Remote(
            
            command_executor="http://127.0.0.1:4723", options=options)
        
        time.sleep(5)

    def wait_for_element(self, locator_type, locator_value, timeout=10):
        """Wait for an element to be present and visible."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
        except Exception as e:
            print(f"Element with {locator_value} not found: {e}")
            return None

    def click_element(self, locator_type, locator_value):
        """Wait and click an element."""
        element = self.wait_for_element(locator_type, locator_value)
        if element:
            try:
                element.click()
            except Exception as e:
                print(f"Error clicking element with {locator_value}: {e}")
        else:
            print(f"Element not found to click with {locator_value}")

    def input_clear(self, locator_type, locator_value, text):
        """Wait and input text into an element."""
        element = self.wait_for_element(locator_type, locator_value)
        if element:
            try:
                element.clear()
                element.send_keys(text)
            except Exception as e:
                print(f"Error inputting text into element with {locator_value}: {e}")
        else:
            print(f"Element not found to input text with {locator_value}")

    def input_text(self, locator_type, locator_value, text):
        """Wait and input text into an element."""
        element = self.wait_for_element(locator_type, locator_value)
        if element:
            try:
                element.send_keys(text)
            except Exception as e:
                print(f"Error inputting text into element with {locator_value}: {e}")
        else:
            print(f"Element not found to input text with {locator_value}")

    def scroll_to_element(self, text):
        """Scroll until the specified element is visible."""
        try:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("{text}");'
            )
        except Exception as e:
            print(f"Error scrolling to element with text {text}: {e}")

    def close(self):
        """Close the session if it's active."""
        if self.driver.session_id:
            self.driver.quit()  # Properly terminate the session if it's active
            print("Session closed successfully.")
        else:
            print("Session not started or already terminated.")

    def perform_action(self):
        try:
            # Click on "Your Schedule"
            self.click_element(
                By.XPATH, '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvRoutine"]/android.widget.LinearLayout'
            )

            # Define the number of days to go after
            days_to_go_after = 2
            for _ in range(days_to_go_after):
                self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/acivNextRoutine")

            # Service date
            self.click_element(
                By.XPATH, '//androidx.cardview.widget.CardView[@resource-id="com.mpower.android.app.lpin.crm:id/mcvTreatement"]/android.widget.LinearLayout/android.widget.ImageView'
            )

            # Select service type
            self.click_element(
                By.XPATH, "//android.widget.TextView[@text='সেবার ধরন']/parent::android.widget.LinearLayout//android.widget.TextView[@text='বাছাই করুন']"
            )
            self.click_element(By.XPATH, "//android.widget.TextView[@text='অসুস্থতার সেবা']")

            # Select animal type
            self.click_element(
                By.XPATH, "//android.widget.TextView[@text='প্রাণী']/parent::android.widget.LinearLayout//android.widget.TextView[@text='বাছাই করুন']"
            )
            self.click_element(By.XPATH, "//android.widget.TextView[@text='গরু']")

            # Select animal's type (বকনা)
            self.click_element(
                By.XPATH, "//android.widget.TextView[@text='প্রাণীর ধরন']/parent::android.widget.LinearLayout//android.widget.TextView[@text='বাছাই করুন']"
            )
            self.click_element(By.XPATH, "//android.widget.CheckedTextView[@text='বকনা']")

            # Select pregnancy status (না)
            self.click_element(
                By.XPATH, "//android.widget.TextView[@text='গর্ভবতী']/parent::android.widget.LinearLayout//android.widget.TextView[@text='বাছাই করুন']"
            )
            self.click_element(By.XPATH, "//android.widget.TextView[@text='না']")

            # Add medicine
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/fabMedicine")
            self.click_element(By.XPATH, "//android.widget.TextView[@text='বাছাই করুন']")
            self.click_element(By.XPATH, "//android.widget.TextView[@text='কিটোসিস']")
            self.click_element(By.XPATH, "//android.widget.TextView[@text='Calcium preparation']")
            self.click_element(By.XPATH, "//android.widget.TextView[@text='Liq. Calplex']")
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/acivSubmitDialog")

            # Scroll and submit medicines
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(1);'
            )
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/mbSubmitMedicine")
            print("checking if code incorrect")
            
            self.click_element(By.XPATH, '//android.widget.ImageView[@resource-id="com.mpower.android.app.lpin.crm:id/btnDialogClose"]')
            self.input_text(By.XPATH, '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/acetNextDayTreatment"]', '5')
            
            self.click_element(By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="1"]')
            self.click_element(By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="2"]')
            self.click_element(By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="AM"]')
            self.click_element(By.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="PM"]')
            
            
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(1);'
            )
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/mbSubmitTreatment")
            print("again checking")
            

        except Exception as e:
            print(f"An error occurred: {e}")
        # finally:
        #     self.close()
