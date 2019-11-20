import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC1
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.tradingview.com/chart/1DrFniL0/")

driver.maximize_window()

ActionChains(driver).key_down(Keys.ALT).send_keys('s').perform()
wait_time = 25
element = WebDriverWait(driver, wait_time).until(EC1.element_to_be_clickable((By.LINK_TEXT, 'Save image')))
element.click()
time.sleep(3)
driver.close()