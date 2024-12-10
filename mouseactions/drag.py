from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

#driver.switch_to.frame()
source=driver.find_element(By.ID, "box6")
target=driver.find_element(By.ID, "box106")

act=ActionChains(driver)
act.drag_and_drop(source, target).perform()


input("Drag and drop hemanth...!")