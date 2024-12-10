from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)

driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYoffset;")

print("Values moved :", value)

# #untill find an element
# script=driver.find_element(By.XPATH, "//*[@id='post-body-3126553095830633702']/div[4]/div[3]/h3")
# driver.execute_script("arguments[0].scrollIntoView();")

input("Scroll bar hemanth...!")