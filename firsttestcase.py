# # steps
# open url (the browser)
# enter user Name
# enter pwd
# click on login
# capture title of the page 
# verify the title of the page 
# close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#to open the browser
#Service_obj = Service("c:\\Windows\\chromedriver.exe")
#driver = webdriver.Chrome("c:\Windows\chromedriver.exe") S3

# Initialize the WebDriver using the Service object
driver = webdriver.Chrome() # WebDriver instance named 'driver'

#open url
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# #find element
# driver.find_element(By.NAME, "username").send_keys("Admin")  # Locate by NAME
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.TYPE, "submit").click()

# Wait for the username input field to be present and visible
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username_field.clear()
username_field.send_keys("Admin")

# Wait for the password field and enter the password
password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")

# Wait for the login button and click it
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

#capture and validate the title
act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("log-in test passed")
else:
    print("log-in test failed")

#close
driver.close()