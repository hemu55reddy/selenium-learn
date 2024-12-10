from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
import time


# service_obj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)

driver=webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
driver.maximize_window()

# #ABX
# driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/form/div[1]/input").send_keys("hemanth")
# driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/form/div[2]/input").send_keys("JOB@hemu55")
# driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input").click()

# #RXp
# driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[1]/input").send_keys("hemanth")
# driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[2]/input").send_keys("JOB@hemu55")
# driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[3]/input").click()

#Contains and strts-with
# driver.find_element(By.XPATH, "//*[contains(@name,'use'])").send_keys("hemanth")
# driver.find_element(By.XPATH, "//*[contains(@name,'pass']/form/div[2]/input)").send_keys("JOB@hemu55")
# driver.find_element(By.XPATH, "//*[contains(@type,'su']/form/div[3]/input)").click()

driver.find_element(By.XPATH, "//*[starts-with(@name,'use'])").send_keys("hemanth")
driver.find_element(By.XPATH, "//*[starts-with(@name,'pass']/form/div[2]/input)").send_keys("JOB@hemu55")
driver.find_element(By.XPATH, "//*[starts-with(@type,'su']/form/div[3]/input)").click()


input("Press enter to close...Hemanth")
driver.quit()