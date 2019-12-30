import pandas as pd
from datetime import date


pd.option_context('display.max_rows', None, 'display.max_columns', None)

data = pd.read_html('https://ca.finance.yahoo.com/quote/V/history')[0]

print(data)