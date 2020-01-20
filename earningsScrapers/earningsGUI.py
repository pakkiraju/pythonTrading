from tkinter import *
from tkinter.tix import *
import csv
from datetime import date
import yahooFinanceToCSV

def ScrolledFrame(parent):
  def on_resize(event):
    bbox = canvas.bbox('all')
    canvas.config(width=bbox[2], scrollregion=bbox)

  # note: Canvas is the outer container
  canvas = tkinter.Canvas(parent)
  # *** modify the below line to suit your layout manager
  canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

  sb = tkinter.Scrollbar(parent, orient=tkinter.VERTICAL, command=canvas.yview)
  # *** modify the below line to use same layout manager as canavas
  sb.pack(side=tkinter.RIGHT, fill=tkinter.Y)

  canvas.config(yscrollcommand=sb.set)

  frame = tkinter.Frame(canvas)
  canvas.create_window(0, 0, window=frame, anchor='nw')
  frame.bind('<Configure>', on_resize)

  return frame


root = Tk()
frame = ScrolledFrame(root)
# open file
with open(r'earnings_{}.csv'.format(date.today()), newline = "") as file:
   reader = csv.reader(file)

   # r and c tell us where to grid the labels
   r = 0
   for col in reader:
      c = 0
      for row in col:
         # i've added some styling
         label = tkinter.Label(frame, width = 30, height = 2, \
                               text = row, relief = tkinter.RIDGE)
         label.grid(row = r, column = c)
         c += 1
      r += 1

root.mainloop()