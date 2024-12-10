from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)


driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button=driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")
act=ActionChains(driver)

act.context_click(button).perform()


input("right click Hemanth...!")