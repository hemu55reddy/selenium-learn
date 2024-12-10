from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.wait import WebDriverWait

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
wait=WebDriverWait(driver, 10)

driver.switch_to.frame("iframeResult")
first=wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/input[1]")))
first.clear()
first.send_keys("hemanth")
button=driver.find_element(By.XPATH, "/html/body/button")

act=ActionChains(driver)

act.double_click(button).perform()


input("Double click Hemanth....!")