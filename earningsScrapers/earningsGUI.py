from tkinter import *
from tkinter.tix import *
import csv
from datetime import date
import yahooFinanceToCSV

root = Tk()

# open file
with open(r'earnings_{}.csv'.format(date.today()), newline = "") as file:
   reader = csv.reader(file)

   # r and c tell us where to grid the labels
   r = 0
   for col in reader:
      c = 0
      for row in col:
         # i've added some styling
         label = tkinter.Label(root, width = 35, height = 2, \
                               text = row, relief = tkinter.RIDGE)
         label.grid(row = r, column = c)
         c += 1
      r += 1

root.mainloop()