from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# soj=service("c:\\Windows\\chromedriver.exe")
# driver=webdriver.Chrome(service=soj)

driver=webdriver.Chrome()
#driver.implicitly_wait(10)
#driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/")
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()


# driver.switch_to.frame("Interaction")
# driver.find_element(By.LINK_TEXT, "Drag And Drop").click()
# driver.switch_to.default_content()

# driver.switch_to.frame("Widgets")
# driver.find_element(By.LINK_TEXT, "DatePicker").click()
# driver.switch_to.default_content()

# driver.switch_to.frame("Miscellaneous")
# driver.find_element(By.XPATH, "Toolbar").click()

#Inner frames
driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()


# Wait and switch to the outer frame
out = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/section/div"))
)
driver.switch_to.frame(out)

# Wait and switch to the inner frame
inn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/iframe"))
)
driver.switch_to.frame(inn)

# Interact with the input field
input_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div/div/input"))
)
input_field.send_keys("hemanth")


input("hey dude...frame")