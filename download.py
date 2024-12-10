from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)
driver.implicitly_wait(10)

# driver.get("http://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.maximize_window()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    soj=Service("c:\\Windows\\chromedriver.exe")

#download the file in desired location
    preference = {"download.default_directory": r"C:\Users\HP\automation\virtual\selenium"}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preference)

    driver=webdriver.Chrome(service=soj, options=ops)
    return driver

driver=chrome_setup()


driver.get("https://www.datablist.com/learn/csv/download-sample-csv-files")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='__next']/main/div[1]/div[2]/div/div/div/article/section/div/ul[2]/li[2]/a[1]").click()



input("donwload a file")