import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.title)
print(driver.session_id)
assert driver.title == "Swag Labs"

print("Test case 1- pass")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element(By.ID,"login-button").click()
time.sleep(1)
driver.find_element(By.ID,"react-burger-menu-btn").click()
time.sleep(2)
driver.find_element(By.ID,"about_sidebar_link").click()
time.sleep(1)
driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
time.sleep(1)
driver.back()
time.sleep(2)
driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Backpack']").click()
time.sleep(2)
driver.find_element(By.NAME,"add-to-cart").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//button[@id='checkout']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys("Ranveer")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys("Singh")
time.sleep(2)
driver.find_element(By.ID,"postal-code").send_keys("1234")
time.sleep(2)
driver.find_element(By.ID,"continue").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='finish']").click()
time.sleep(2)
driver.find_element(By.ID,"back-to-products")
time.sleep(2)
#driver.find_element(By.CSS_SELECTOR,".product_sort_container")
time.sleep(1)
driver.close()