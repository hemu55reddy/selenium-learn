from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By

# soj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=soj)
driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
#print(driver.page_source)

input("press enter to close..")