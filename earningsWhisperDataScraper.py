import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.earningswhispers.com/calendar")

earningsList = driver.find_element_by_id('epscalendar')
dataOutput = earningsList.text
 print(time.now())
fileName = 'earnings_{}.csv'.format(date.today())

with open(fileName + ".csv", mode='w') as csv_file:
    writer = csv.writer(csv_file)
    finalOutput = re.sub(r"Beat\nMeet\nMiss", "\n", dataOutput)
    writer.writerow(finalOutput)

print(finalOutput)
driver.close()
