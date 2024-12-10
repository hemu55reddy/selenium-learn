from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1 Count no.of rows & columns
#2 read specific rows and columns data
#3 read all coulmns and rows data
#4 read data base on conditions

#1 Count no.of rows & columns
noofrows=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
print("Total rows :", noofrows)

noofcolumn=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//th"))
print("Total Cloumns :", noofcolumn)

#2 read specific rows and columns data
value=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(value)

#3 read all coulmns and rows data
print("All the no. of rowa and columns data:")
# for r in range(2, noofrows+1): #we use one here ncoz N+1
#     for c in range(1, noofcolumn+1):
#         value=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(value, end='  ')
#     print()

#4 read data base on conditions
for r in range(2, noofrows+1):
    author=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author=="Mukesh":
        book=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(book,"     ",author,"   ",price)



input("Its static table data hemanth...!")