from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

import time


# ser_obj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)

driver=webdriver.Chrome()
#driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME, 'q')
searchbox.send_keys("Selenium")
searchbox.submit()

#driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3").click()
wait=WebDriverWait(driver, 20, ignored_exceptions=[NoSuchElementException, ElementNotInteractableException, Exception])
selenium=wait.until(EC.presence_of_element_located((By.XPATH, ("//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3"))))
selenium.click()
input("Please close dude...")