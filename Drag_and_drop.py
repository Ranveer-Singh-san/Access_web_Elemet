import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Actions/index.html#")
driver.maximize_window()

source=driver.find_element(By.XPATH,"//div[@id='draggable']")
destination=driver.find_element(By.XPATH,"//div[@id='droppable']")

# create action chain object
actions = ActionChains(driver)

# Perform drag and drop
actions.drag_and_drop(source, destination).perform()
time.sleep(2)

Perform_double_click=driver.find_element(By.XPATH,"//div[@id='double-click']")
action = ActionChains(driver)
# Perform double-click
actions.double_click(Perform_double_click).perform()

time.sleep(2)

Click_on_dropdown=driver.find_element(By.XPATH,"//button[normalize-space()='Hover Over Me Third!']")
Click_on_dropdown.click()
time.sleep(2)
abc = wait.until(EC.element_to_be_clickable(By.XPATH,"//a[@class='list-alert' and text()='Link 1']"))




# alert = driver.switch_to.alert
# alert.accept()
# driver.close()