from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ddt import XLUtils


soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)
wait=WebDriverWait(driver, 10)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username_field.clear()
username_field.send_keys("Admin")

# Wait for the password field and enter the password
password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")

# Wait for the login button and click it
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li"))).click()



input("Dinamic Tables Hemanth...!")