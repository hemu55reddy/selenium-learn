from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# soj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=soj)
driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

wait=WebDriverWait(driver, 20)
#driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a")
lc=wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "OrangeHRM, Inc")))
lc.click()


time.sleep(5)
#driver.close()
driver.quit()
input("enter....")