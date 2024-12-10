from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Wishlist").click()

val=driver.title
act="nopCommerce demo store. Wishlist"

if val==act:
    print("Hemanth u have done it!")
else:
    print("Not the correct one")


driver.close()