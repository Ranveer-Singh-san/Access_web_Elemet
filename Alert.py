import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()

driver.get("https://webdriveruniversity.com/Page-Object-Model/index.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@class='btn btn-secondary center-block']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='btn btn-default'][1]").click()
time.sleep(2)
driver.close()