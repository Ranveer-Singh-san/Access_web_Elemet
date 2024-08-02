import time
from telnetlib import EC

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Popup-Alerts/index.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@onclick='myFunction()']").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='btn btn-default btn-lg dropdown-toggle']").click()
time.sleep(3)
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(3)
# driver.find_element(By.XPATH,"//a[normalize-space()='CLICK ME!']").click()
# wait = WebDriverWait(driver, 10)  # 10 seconds timeout
# loader= wait.until(EC.invisibility_of_element_located((By.XPATH,"//div[@class='ajax-loader']")))
# wait = WebDriverWait(driver, 10)  # 10 seconds timeout
# driver.close()

driver.find_element(By.XPATH,"(//span[@id='button4'])").click()
time.sleep(1)
alert = driver.switch_to.alert
time.sleep(1)
alert.accept()
