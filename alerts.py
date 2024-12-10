from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

# soj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=soj)

driver=webdriver.Chrome()

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()

# #Open alert window
# driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
# time.sleep(5)

# alert=driver.switch_to.alert
# print(alert.text)

# alert.send_keys('Hemanth')

# #alert.accept()
# alert.dismiss()
# driver.get("https://mypage.rediff.com/login/dologin")
# driver.maximize_window()

# driver.find_element(By.XPATH, "//*[@id='pass_div']/input[3]").click()
# ok=driver.switch_to.alert
# print(ok.text)
# ok.accept()

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth") #by pass values in url
driver.maximize_window()



input("Good Morning...!")