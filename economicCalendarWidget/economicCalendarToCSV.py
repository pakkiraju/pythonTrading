import pandas as pd
from datetime import date


# Forcing Pandas to display max rows and columns.
pd.option_context('display.max_rows', None, 'display.max_columns', None)
# Reading the earnings calendar table on yahoo finance website.
earnings = pd.read_html('https://finance.yahoo.com/calendar/economic/')[0]
# Writing to a CSV file.
earnings.to_csv(r'economicCalendar_{}.csv'.format(date.today()), index=None)