from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


soj=Service("c:\\Windows\\chromedriver.exe")
driver=webdriver.Chrome(service=soj)

#driver.get("https://jqueryui.com/datepicker/") # 1 and 2 types
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()


# #switch to frame
# driver.switch_to.frame(0)  # o is an index

# #first type
# # mm/dd/yyyy
# #driver.find_element(By.ID, "datepicker").send_keys("07/22/1998")


# #second type
# year="2023"
# month="July"
# date="15"
# driver.find_element(By.ID, "datepicker").click()

# #While loop
# while True:
#     mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
#     yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

#     if mon==month and yr==year:
#         break;
#     else:
#         driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()

# #select date
# dt=driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

# for d in dt:
#     if d.text==date:
#         d.click()
#         break


driver.find_element(By.XPATH, "//*[@id='dob']").click()

dp_month=Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
dp_month.select_by_visible_text("Jul")

dp_year=Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
dp_year.select_by_visible_text("1998")

dt=driver.find_elements(By.XPATH, "//table[@class = 'ui-datepicker-calendar']//tbody/tr/td/a")

for d in dt:
    if d.text=="22":
        d.click()
        break;



input("Date picker Hemanth...!")