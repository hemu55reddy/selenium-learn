from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# soj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=soj)

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
wait=WebDriverWait(driver, 10)

wid=driver.current_window_handle
#print(wid)

wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a"))).click()
wids=driver.window_handles
#print(wids)

# pwid=wids[0]
# cwid=wids[1]

# print(pwid, cwid)


# driver.switch_to.window(cwid)
# print("Chile ", driver.title)

# driver.switch_to.window(pwid)
# print("parent ", driver.title)

#loop approach
for w in wids:   #switch btw beowsers
    driver.switch_to.window(w)
    if driver.title=="Human Resources Management Software | OrangeHRM":
        driver.close()

    #print(driver.title)


input("Multiple tabs....")

#testautomationpractice.blogspot.com