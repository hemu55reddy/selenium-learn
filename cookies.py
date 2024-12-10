from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import os

soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)
driver.implicitly_wait(10)


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#capture cookies
# cookies=driver.get_cookies()
# print(len(cookies))

# for c in cookies:
#     #print(c)
#     #print(c.get('name'))
#     print(c.get('name'),":",c.get('value'))

#add new cookies
driver.add_cookie({'name':"Hemanth",'value':"12345"})

cookies=driver.get_cookies()
print("size of cookies after adding : ", len(cookies))
# for c in cookies:
#     print(c)
#     print(c.get('name'))

#Delete specifi cookie from the browser
driver.delete_cookie('Hemanth')

cookies=driver.get_cookies()
print("size of cookies deleting cookie : ", len(cookies))
# for c in cookies:
#     print(c)
#     print(c.get('name'))

#Delete All cookie from the browser
driver.delete_all_cookies()

cookies=driver.get_cookies()
print("size of cookies deleting all cookies : ", len(cookies))
# for c in cookies:
#     print(c)
#     print(c.get('name'))


input("Cookies Hemanth....!")