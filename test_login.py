import selenium
from selenium.webdriver import Chrome
from selenium import webdriver
import allure
#from allure.constants import AttachmentType
from allure_commons.types import AttachmentType
@allure.severity(allure.severity_level.NORMAL)
def test_url():
    path = "D:\chromedriver_win32 (1)\chromedriver.exe"
    driver = Chrome(executable_path=path)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.get("https://www.hdfcbank.com/")
    driver.maximize_window()
