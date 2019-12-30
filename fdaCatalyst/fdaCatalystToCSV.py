import pandas as pd
# from datetime import date
#
# # Forcing Pandas to display max rows and columns.
# pd.option_context('display.max_rows', None, 'display.max_columns', None)
# # Reading the earnings calendar table on yahoo finance website.
# earnings = pd.read_html('https://www.biopharmcatalyst.com/calendars/fda-calendar')[0]
# # Writing to a CSV file.
# earnings.to_csv(r'fdaCatalyst_{}.csv'.format(date.today()), index=None)

import requests

url = 'https://www.biopharmcatalyst.com/calendars/fda-calendar'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)

dfs = pd.read_html(r.text)
print(dfs)