from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)
driver.implicitly_wait(10)


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()


#driver.save_screenshot("C:\\Users\\HP\\automation\\virtual\\selenium\\mysshot.png") #(os.getcwd+"\\mysshot.png")
driver.get_screenshot_as_file(os.getcwd() + "\\homepage.png")