import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "platformName": "android",
    "deviceName": "oneplus",
    "app": r"C:\Users\157578\Downloads\khan-academy-7-3-2.apk",
    #"udid":"emulator-5554"
}

driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

print(driver.page_source)

time.sleep(5)
driver.quit()
