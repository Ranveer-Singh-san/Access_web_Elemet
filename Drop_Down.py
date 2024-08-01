import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

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
time.sleep(5)

select=Select(driver.find_element(By.CSS_SELECTOR,".product_sort_container"))

time.sleep(2)
select.select_by_value('za')
time.sleep(2)
print(select)
select=Select(driver.find_element(By.CSS_SELECTOR,".product_sort_container"))
time.sleep(2)
select.select_by_index(3)
time.sleep(2)
select=Select(driver.find_element(By.CSS_SELECTOR,".product_sort_container"))
time.sleep(2)
select.select_by_visible_text('Price (low to high)')
time.sleep(2)

driver.close()