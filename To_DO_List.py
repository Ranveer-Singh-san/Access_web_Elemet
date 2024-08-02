import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


driver.get("https://webdriveruniversity.com/To-Do-List/index.html")
driver.maximize_window()
time.sleep(2)

Add_item= driver.find_element(By.XPATH,"//input[@placeholder='Add new todo']")
Add_item.send_keys("RAM")
Add_item.send_keys(Keys.RETURN)  #Press Enter
time.sleep(2)

delate_item=driver.find_element(By.XPATH,"//li[normalize-space()='RAM']").click()
time.sleep(2)

driver.close()