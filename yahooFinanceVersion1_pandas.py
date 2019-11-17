import csv
import pandas as pd
from datetime import date, datetime

earnings = pd.read_html('https://finance.yahoo.com/calendar/earnings')[0]

# if datetime.now().strftime("%H%M%S") >= "090000":
#     fileName = 'AMC_earnings_{}'.format(date.today())
# elif datetime.now().strftime("%H%M%S") < "090000":
#     fileName = 'BMO_earnings_{}'.format(date.today())

fileName = "yahooFinance_Pandas"
with open(fileName + ".csv", mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([earnings])

print(earnings)

# import pandas as pd
# url = r'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
# tables = pd.read_html(url) # Returns list of all tables on page
# sp500_table = tables[0] # Select table of interest
# print(sp500_table)