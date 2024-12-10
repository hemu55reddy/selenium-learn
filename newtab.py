from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import os

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)
driver.implicitly_wait(10)

# #open a tab in another page
# driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/")
# driver.maximize_window()


# about=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.XPATH, "//*[@id='menu-item-53896']/a").send_keys(about)

#2 apps in different tabs
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/")
#driver.switch_to.new_window('tab')#new tab
driver.switch_to.new_window('window')#new window
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


input("New tab...")