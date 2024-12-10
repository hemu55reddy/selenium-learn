from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min=driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
max=driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print("Position before drag...")


print("Min location is :", min.location)
print("max location is :", max.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(min,100,0).perform()
act.drag_and_drop_by_offset(max,-50,0).perform()

input("sliders Hemanth...!")