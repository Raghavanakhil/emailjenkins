import selenium
from selenium.webdriver import Chrome
from selenium import webdriver


def test_url():
    path = "D:\chromedriver_win32 (1)\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.hdfcbank.com/")
    driver.maximize_window()
