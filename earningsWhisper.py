import csv
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date, time, datetime

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.earningswhispers.com/calendar")

earningsList = driver.find_element_by_id('epscalendar')
dataOutput = earningsList.text

if datetime.now().strftime("%H%M%S") >= "090000":
    fileName = 'AMC_earnings_{}'.format(date.today())
elif datetime.now().strftime("%H%M%S") < "090000":
    fileName = 'BMO_earnings_{}'.format(date.today())

with open(fileName + ".csv", mode='w') as csv_file:
    writer = csv.writer(csv_file)
    finalOutput = re.sub(r"Beat\nMeet\nMiss", "\n", dataOutput)
    # finalOutput = re.sub(r"Company\nEstimate\nActual\nGrowth\nGuidance\nScore\nSurprise\n", "\n", dataOutput)
    writer.writerow([finalOutput])

print(finalOutput)
driver.close()
