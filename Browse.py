import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://saucelabs.com/request-demo")
driver.maximize_window()
print(driver.title)
print(driver.session_id)
assert driver.title == "Request a Sauce Labs Demo"

print("Test case 1- pass")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("Abc@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='Company']").send_keys("ABC")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='Phone']").send_keys("1234567890")
time.sleep(2)
select=Select(driver.find_element(By.XPATH,"//select[@id='Solution_Interest__c']"))
time.sleep(2)
select.select_by_index(4)
time.sleep(2)


driver.save_screenshot('screenshot.png')
driver.save_screenshot('screenshot.png')


driver.find_element(By.XPATH,"//textarea[@id='Sales_Contact_Comments__c']").send_keys("Team testing")
time.sleep(2)
driver.find_element(By.XPATH,"//label[@id='LblmktoCheckbox_42368_0']").click()
time.sleep(2)
driver.close()