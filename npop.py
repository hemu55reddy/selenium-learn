from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj, options=ops)

driver.get("http://whatmyloaction.com/")
driver.maximize_window()

