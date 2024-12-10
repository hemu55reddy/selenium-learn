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
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()
wait=WebDriverWait(driver, 10)
#driver.implicitly_wait(10)
#single check box
#driver.find_element(By.XPATH, "//*[@id='profession-1']").click()

#Multiple chekboxes
#checkboxes=driver.find_elements(By.XPATH, "//div[@class='col-md-9 col-sm-12'")
checkboxes=wait.until(ec.visibility_of_all_elements_located((By.XPATH, "//input[@type='checkbox' and contains(@class, 'custom-control-input')]")))

print(len(checkboxes))

# for i in range(len(checkboxes)):
#     checkboxes[i].click()
#AP2
# for checkbox in checkboxes:
#     checkbox.click()


#Multiple chekboxes by choice
# for checkbox in checkboxes:
#     week=checkbox.get_attribute('attr')
#     if week=='mday' or week=='sday':
#      checkbox.click()

# #select last 2 checkboxes
# for i in range(len(checkboxes)-2, len(checkboxes)):
#    checkboxes[i].click()

#select first 2 checkboxes
# for i in range(len(checkboxes)):
#    if i<2:
#      checkboxes[i].click()


#Clear all
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()

input("Hello u r done..!")