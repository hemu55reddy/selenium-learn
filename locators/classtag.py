from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#cl=driver.find_elements(By.CLASS_NAME, "")
tag=driver.find_elements(By.TAG_NAME, "a")
print(len(tag))