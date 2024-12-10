from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome import service
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# ser_obj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=ser_obj)

driver=webdriver.Chrome()
driver.get("https://www.telerik.com/support/demos")
driver.maximize_window()
wait=WebDriverWait(driver, 10)

#driver.find_element(By.LINK_TEXT, "Digital link").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()


#find no. of elements in a page
links=driver.find_elements(By.TAG_NAME, "a")
print("Total links:",(len(links)))

for i in links:
    print(i.text)
input("..")