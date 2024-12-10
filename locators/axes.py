from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By

so=service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=so)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()


