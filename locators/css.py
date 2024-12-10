from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

#tag & ID
# e=driver.find_element(By.CSS_SELECTOR, "input#email")
# e.send_keys("hemanth")

#Tag & Class
# e=driver.find_element(By.CSS_SELECTOR, "input.inputtext")
# e.send_keys("hemanth@gmail.com")

#Tag & attribute
# e=driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]")
# e.send_keys("hemanth@gmail.com")

#Tag, Class and Attribute
e=driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]")
e.send_keys("hemanth@gmail.com")

enter=e.get_attribute("value")

if enter == "hemanth@gmail.com":
    print("Success")
else:
    print("Fail")