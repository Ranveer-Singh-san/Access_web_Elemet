import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key,Controller


driver = webdriver.Chrome()
driver.get("https://www.filestack.com/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "fsp-select-labels").click()
time.sleep(1)

keyword = Controller()
keyword.type("C:\\ran.jpg")
time.sleep(1)
keyword.press(Key.enter)
keyword.release(Key.enter)
time.sleep(1)
driver.close()














