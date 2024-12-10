from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from XLUtils import *  # assuming XLUtils functions are working correctly

import time


soj = Service("c:\\Windows\\chromedriver.exe")
driver = webdriver.Chrome(service=soj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

file = "C:\\Users\\HP\\Downloads\\period_data.xlsx"
rows = getRowCount(file, "Sheet")

for r in range(2, rows + 1):
    princ = readData(file, "Sheet", r, 1)
    roi = readData(file, "Sheet", r, 2)
    p1 = readData(file, "Sheet", r, 3)
    p2 = readData(file, "Sheet", r, 4)
    frequency = readData(file, "Sheet", r, 5)
    expm = readData(file, "Sheet", r, 6)

    # Pass the values
    driver.find_element(By.XPATH, "//*[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH, "//*[@id='interest']").send_keys(roi)
    driver.find_element(By.XPATH, "//*[@id='tenure']").send_keys(p1)

    # Dropdown for tenure period
    perioddrp = Select(driver.find_element(By.XPATH, "//*[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(p2)

    # Dropdown for frequency
    frqdp = Select(driver.find_element(By.XPATH, "//*[@id='frequency']"))
    frqdp.select_by_visible_text(frequency)
    
    # Wait for the overlay to disappear (if present)
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "wzrk-overlay")))
    
    # Wait for the button to be clickable and click it
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div[2]/div/div[5]/div/div[1]/div[3]/form/div[2]/a[1]/img")))
    button.click()

    # Capture the actual value
    act_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # Validation
    if float(expm) == float(act_value):
        print("Test is passed")
        writeData(file, "Sheet", r, 8, "Passed")
    else:
        print("Test Failed")
        writeData(file, "Sheet", r, 8, "Failed")

    # Click the reset button
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()

    # Adding sleep for a moment to allow for any animations/processing
    time.sleep(10)

driver.quit() 
