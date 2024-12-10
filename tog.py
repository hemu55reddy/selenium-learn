from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)

driver.get("https://www.semrush.com/blog/google-tag-manager/")
driver.maximize_window()

tog=driver.find_element(By.XPATH, "//*[@id='__next']/div/header/nav/div[2]/div/div/div[3]/div[2]/label[1]/span/div")

time.sleep(5)
tog.click()


input("Toggle...Hemanth")