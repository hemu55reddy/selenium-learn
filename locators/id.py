from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")

driver.find_element(By.ID, "small-searchterms").send_keys('Laptop')
driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

title=driver.title
exp_title="nopCommerce demo store. Search"


if title==exp_title:
    print("Hemanth u got it")
else:
    print("Try again")