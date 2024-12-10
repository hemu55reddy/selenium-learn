from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import service
from selenium.webdriver.support.ui import Select
import time
# soj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=soj)
driver=webdriver.Chrome()

driver.get("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
driver.maximize_window()

wait=WebDriverWait(driver, 10)

country=wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/select[1]")))
element=Select(country)

# select opt from the dp
#element.select_by_visible_text("Python")
#element.select_by_value("sql")
#element.select_by_index(2)

#total options
alloptions=element.options
print("Total options are :", len(alloptions))

# #value r title of the option
for i in alloptions:
    print("This option is: ", i.text)

#select opt without using inbuilt
for i in alloptions:
    if i.text=="SQL":
        i.click()

input("Come on dude..!")