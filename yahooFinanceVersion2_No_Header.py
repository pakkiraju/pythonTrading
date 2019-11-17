import csv
from urllib2 import Request, urlopen, URLError
from TableParser import TableParser
url_addr ='https://finance.yahoo.com/calendar/earnings?day=2019-11-19'
req = Request(url_addr)
url = urlopen(req)
tp = TableParser()
tp.feed(url.read())

# NOTE: Here you need to know exactly how many tables are on the page and which one
# you want. Let's say it's the first table
my_table = tp.get_tables()[0]
filename = 'yahooFinance_noHeader.csv'
f = open(filename, 'wb')
with f:
    writer = csv.writer(f)
    for row in my_table:
        writer.writerow(row)