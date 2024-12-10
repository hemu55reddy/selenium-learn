from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)

driver.get("https://practice.expandtesting.com/hovers")
driver.maximize_window()

user=driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[3]/img")
profile=driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[3]/div/a")

#Chain
action=ActionChains(driver)
action.move_to_element(user).move_to_element(profile).click().perform()



input("Ur mouse got hovered....!")