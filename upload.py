from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)
driver.implicitly_wait(10)

driver.get("https://ps.uci.edu/~franklin/doc/file_upload.html")
driver.maximize_window()


driver.find_element(By.XPATH, "/html/body/form/input[1]").send_keys(
    r"C:\Users\HP\automation\virtual\selenium\customers-1000.csv"
)


input("Upload a file buddy..!")