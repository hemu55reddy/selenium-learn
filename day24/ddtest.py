from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from XLUtils import *
from day24 import XLUtils

import time


soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file="C:\\Users\\HP\\Downloads\\period_data.xlsx"
rows=XLUtils.getRowCount(file, "Sheet")

for r in range(2,rows+1):
    princ=XLUtils.readData(file, "Sheet", r,1)
    roi=XLUtils.readData(file, "Sheet", r,2)
    p1=XLUtils.readData(file, "Sheet", r,3)
    p2=XLUtils.readData(file, "Sheet", r,4)
    frequency=XLUtils.readData(file, "Sheet", r,5)
    expm=XLUtils.readData(file, "Sheet", r,6)

    #Pass the values
    driver.find_element(By.XPATH, "//*[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH, "//*[@id='interest']").send_keys(roi)
    driver.find_element(By.XPATH, "//*[@id='tenure']]").send_keys(p1)
#Dropdown
    perioddrp = Select(driver.find_element(By.XPATH, "//*[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(p2)

    frqdp=Select(driver.find_element(By.XPATH, "//*[@id='frequency']"))
    frqdp.select_by_visible_text(frequency)
    
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    

    act_value=driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    #Validation
    if float(expm)==float(act_value):
        print("Test is passed")
        XLUtils.writeData(file, "Sheet", r, 8, "Passed")
    else:
        print("Test Failed")
        XLUtils.writeData(file, "Sheet", 8, "Failed")
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()

    time.sleep(10)