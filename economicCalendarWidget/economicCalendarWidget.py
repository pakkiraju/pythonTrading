from tkinter.tix import *
import csv
from datetime import date
import economicCalendarToCSV
import os

def ScrolledFrame(parent):
  def on_resize(event):
    bbox = canvas.bbox('all')
    canvas.config(width=bbox[2], scrollregion=bbox)

  def on_mouse_wheel(event):
    # better checking whether event happens inside frame
    canvas.yview_scroll(event.delta//-30, 'units')

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
  # use bind_all() to make sure mouse wheel events can be triggered
  # even the canvas is filled with labels on top
  canvas.bind_all('<MouseWheel>', on_mouse_wheel)

  return frame


root = Tk()
root.title("Today's Economic Calendar via Yahoo!")
path = os.getcwd()
root.iconbitmap(path+"\ICONS\Sicons-Basic-Round-Social-Yahoo.ico")
frame = ScrolledFrame(root)
# open file
with open(r'economicCalendar_{}.csv'.format(date.today()), newline = "") as file:
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