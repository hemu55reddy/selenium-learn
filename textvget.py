from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# soj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=soj)
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/login")


#c=driver.find_element(By.XPATH, "//*[@id='Email']]")
wait=WebDriverWait(driver, 20)
#c=wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='Email']")))
c=wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button")))
#c.clear()
c.send_keys("hemanth@gmail.com")
print("res of text:", c.text)
print("res of attribute:", c.get_attribute('type'))
p=driver.find_element(By.XPATH, "//*[@id='Password']")

p.clear()

input("please close..!")