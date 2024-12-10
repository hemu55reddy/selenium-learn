from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests

# ser_obj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)

driver=webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
wait=WebDriverWait(driver, 10)

#we have to install requets module from .py

tlinks=driver.find_elements(By.TAG_NAME, "a")
count=0

for link in tlinks:
    url=link.get_attribute('href')
    try:
     res=requests.head(url)
    except:
       None
    if res.status_code>=400:
        print(url, "Is a broken link")
        count+=1
    else:
        print(url, "Is a valid link")


print("Total no. of links", count)

input("Dude got it...!")