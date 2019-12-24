###############################################################################
### Creator         : Pradhamesh Akkiraju                                   ###
### Date            : December 23/2019                                      ###
### Project Name    : rangeBreakV2                                          ###
### Description     : This is a target, share, loss calculator              ###
###                   based on a range break that is specified by the user  ###
###############################################################################

# Imports
import tkinter as tk
from tkinter import messagebox

# Create a function for the short side that contains all the formulas
def longCalc():
    tk.Label(window, text="# of Shares").grid(row=4, column=0)
    tk.Label(window, text="Execution Price").grid(row=4, column=1)
    tk.Label(window, text="Targets").grid(row=4, column=2)
    tk.Label(window, text="Potential Profit").grid(row=4, column =3)

window = tk.Tk()
window.geometry("500x300")
window.title("Range Break V2")

riskText = tk.Label(window, text="Enter Risk").grid(row=0, column=0)
riskInput = tk.Entry(window).grid(row=0, column=1)

rangeHighText = tk.Label(window, text="Enter Range High").grid(row=1, column=0)
rangeHighInput = tk.Entry(window).grid(row=1, column=1)

rangeLowText = tk.Label(window, text="Enter Range Low").grid(row=2, column=0)
rangeLowInput = tk.Entry(window).grid(row=2, column=1)

longButton = tk.Button(window, text="Long", command=longCalc).grid(row=3, column=0)
shortButton = tk.Button(window, text="Short").grid(row=3, column=1)
quitButton = tk.Button(window, text="Quit", command=window.quit).grid(row=3, column=2)

window.mainloop()