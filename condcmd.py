from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# soj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=soj)
driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# #is dispalyed  and is_enabled
# dis=driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input]")
# print(dis.is_displayed())

wait = WebDriverWait(driver, 20)
dis = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")))
print("Element Status")
print("Dis Status:", dis.is_displayed())
print("Enb Status:", dis.is_enabled())

#for radio and check box
driver.get("https://demo.nopcommerce.com/register")
rdm=driver.find_element(By.XPATH, "//*[@id='gender-male']")
rdf=driver.find_element(By.XPATH, "//*[@id='gender-female']")
print("Default Element Status before click")
print("RDM status:", rdm.is_selected())
print("RDF Status:", rdf.is_selected())

rdm.click()

print("Element Status After click Male")
print("Radio RDM staus:", rdm.is_selected())
print("Radio RDF staus:", rdf.is_selected())

rdf.click()
print("Element Status after click Female")
print("Radio RDM staus:", rdm.is_selected())
print("Radio RDF staus:", rdf.is_selected())

input("press enter")