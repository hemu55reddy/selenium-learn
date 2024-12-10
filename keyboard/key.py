from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

#Ctrl+A, C , tab and V
input1=driver.find_element(By.XPATH, "//*[@id='inputText1']")
input2=driver.find_element(By.XPATH, "//*[@id='inputText2']")

input1.send_keys("Hi Hemanth welcome to the automation")

act=ActionChains(driver)

#Ctrl+A
act.key_down(Keys.CONTROL)
act.send_keys("a")

act.key_up(Keys.CONTROL)
act.perform()

#Ctrl+C
act.key_down(Keys.CONTROL)
act.send_keys("c")

act.key_up(Keys.CONTROL)
act.perform()

#Tab
act.send_keys(Keys.TAB).perform()

#Ctrl+V
act.key_down(Keys.CONTROL)
act.send_keys("v")

act.key_up(Keys.CONTROL)
act.perform()

input("Keyboard actions Hemanth....!")