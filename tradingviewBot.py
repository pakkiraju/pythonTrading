import time
import pyautogui, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

ticker = input("Enter ticker:")
driver = webdriver.Chrome()
driver.get("https://www.tradingview.com")

driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[4]/span[2]/a").click()

try:
    usernameInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

finally:
    usernameInput.send_keys("pakkiraju002")

try:
    passwordInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
finally:
    passwordInput.send_keys("Psonu2307*")

driver.find_element_by_xpath("//*[@id='signin-form']/div[3]/div[2]/button/span[2]").click()



try:
    query = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[3]/form/label"))
    )
    time.sleep(2)
finally:
    query.send_keys(ticker)
    query.send_keys(u'\ue007')

try:
    chartButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='js-category-content']/div/div/div/div/div[1]/div/div[1]/div/a"))
    )

finally:
    chartButton.click()
time.sleep(5)

pyautogui.moveTo(500, 500)
pyautogui.click()


#send_keys('s').perform()
driver.close()

