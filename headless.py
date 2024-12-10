from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import os

# soj=Service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=soj)
# driver.implicitly_wait(10)

def headless_chrome():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    soj=Service("c:\\Windows\\chromedriver.exe")
    ops=Options()
    ops.headless = True
    driver=webdriver.Chrome(service=soj, options=ops)

    return driver

driver=headless_chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
print(driver.title)
print(driver.current_url)


input("headless testing hemanth....!")