from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Farmer:
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

    def wait_for_element(self, locator_type, locator_value):
        """Wait for an element to be present and visible."""
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((locator_type, locator_value))
        )


    def click_element(self, locator_type, locator_value):
        """Wait and click an element."""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((locator_type, locator_value))
        )
        element.click()

    def input_text(self, locator_type, locator_value, text):
        """Wait and input text into an element."""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )
        element.send_keys(text)
    
    def input_clear(self, locator_type, locator_value, text):
        """Wait and input text into an element."""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )
        element.clear()
        element.send_keys(text)

    def close(self):
        self.driver.quit()

    def perform_action(self):
        try:
            # searching profile"
            self.click_element(
                "xpath",
                '//android.widget.ImageButton[@content-desc="nv_open"]',
            )

            # click on farmer profile
            self.click_element(
                By.XPATH,
                "//android.widget.TextView[@text='খামারির তালিকা']",
            )

          

        except Exception as e:
            print(f"An error occurred: {e}")
