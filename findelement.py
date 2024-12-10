from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# soj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=soj)
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/register")

#locator matching with single element
#driver.find_element(By.XPATH, "//*[@id='small-searchterms']").send_keys("Laptop")

#locator matching with multiple element
# element=driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(element.text)

#locator not available element
# element=driver.find_element(By.LINK_TEXT, "Login") #incorrect attribute value
# print(element.text)


#elements
#lements=driver.find_elements(By.XPATH, "//*[@id='Email']")
# wait=WebDriverWait(driver, 20)
# elements=wait.until(EC.visibility_of_all_elements_located((By.XPATH, ("//*[@id='small-searchterms']]//a"))))
# print(len(elements))
# print(elements[0].send_keys("dhadhamhemanth@gmail.com"))

#multiple
# elements=driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(elements))
# #print(elements.text)
# for i in elements:
#     print(i.text)

#locator not available element
elements=driver.find_elements(By.LINK_TEXT, "Login") #incorrect attribute value
print(len(elements))
input("Enter to close...!")