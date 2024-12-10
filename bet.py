from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://192.168.0.240:8501/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Wait for and interact with elements
wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/div/div/section[1]/div[1]/div[2]/div/div/div/div/div[3]/div/div/div/input"))).send_keys("Hemanth")
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='number_input_2']"))).send_keys("200")
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='text_area_3']"))).send_keys("Match will end on the 3rd day")
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div[1]/div/div/section[1]/div[1]/div[2]/div/div/div/div/div[7]/div/button/div/p"))).click()

time.sleep(5)
driver.refresh()
input("wait...!")
