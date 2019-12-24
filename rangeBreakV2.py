###############################################################################
### Creator         : Pradhamesh Akkiraju                                   ###
### Date            : December 23/2019                                      ###
### Project Name    : rangeBreakV2                                          ###
### Description     : This is a target, share, loss calculator              ###
###                   based on a range break that is specified by the user  ###
###############################################################################

# Imports
from tkinter import *

# Create a function for the short side that contains all the formulas
def longCalc():
    longRangeHigh = rangeHigh.get()
    longRangeLow = rangeLow.get()
    longRisk = RISK.get()
    rangeWidth = longRangeHigh - longRangeLow

    longShareSize = round(longRisk/rangeWidth, -1)
    Label(window, text=longShareSize).grid(row=8, column=0)

    longEntry = longRangeHigh + 0.01
    Label(window, text=longEntry).grid(row=10, column=0)

    positionValue = round(longEntry * longShareSize, 2)
    Label(window, text=positionValue).grid(row=8, column=1)

    totalLongRisk = round(longShareSize * (longEntry - longRangeLow), 2)
    Label(window, text=totalLongRisk).grid(row=10, column=2)

    longStop = longRangeLow
    Label(window, text=longStop).grid(row=10, column=1)

    longTargetOne = longEntry + rangeWidth
    longTargetTwo = longTargetOne + rangeWidth
    Label(window, text=longTargetOne).grid(row=5, column=1)
    Label(window, text=longTargetTwo).grid(row=6, column=1)

    exitLongSizeOne = round(longShareSize/2, -1)
    Label(window, text=exitLongSizeOne).grid(row=5, column=0)
    exitLongSizeTwo = longShareSize - exitLongSizeOne
    Label(window, text=exitLongSizeTwo).grid(row=6, column=0)

    longProfitOne = round((longTargetOne - longEntry) * exitLongSizeOne, 2)
    longProfitTwo = round((longTargetTwo - longEntry) * exitLongSizeTwo, 2)
    Label(window, text=longProfitOne).grid(row=5, column=2)
    Label(window, text=longProfitTwo).grid(row=6, column=2)

    totalLongProfit = round(longProfitOne + longProfitTwo, 2)
    Label(window, text=totalLongProfit).grid(row=8, column=2)

def shortCalc():
    shortRangeHigh = rangeHigh.get()
    shortRangeLow = rangeLow.get()
    shortRisk = RISK.get()
    rangeWidth = shortRangeHigh - shortRangeLow

    shortShareSize = round(shortRisk/rangeWidth, -1)
    Label(window, text=shortShareSize).grid(row=8, column=0)

    shortEntry = shortRangeLow - 0.01
    Label(window, text=shortEntry).grid(row=10, column=0)

    positionValue = round(shortEntry * shortShareSize, 2)
    Label(window, text=positionValue).grid(row=8, column=1)

    totalShortRisk = round(shortShareSize * (shortRangeHigh - shortEntry), 2)
    Label(window, text=totalShortRisk).grid(row=10, column=2)

    shortStop = shortRangeHigh
    Label(window, text=shortStop).grid(row=10, column=1)

    shortTargetOne = shortEntry - rangeWidth
    shortTargetTwo = shortTargetOne - rangeWidth
    Label(window, text=shortTargetOne).grid(row=5, column=1)
    Label(window, text=shortTargetTwo).grid(row=6, column=1)

    exitShortSizeOne = round(shortShareSize/2, -1)
    Label(window, text=exitShortSizeOne).grid(row=5, column=0)
    exitShortSizeTwo = shortShareSize - exitShortSizeOne
    Label(window, text=exitShortSizeTwo).grid(row=6, column=0)

    shortProfitOne = round((shortEntry - shortTargetOne) * exitShortSizeOne, 2)
    shortProfitTwo = round((shortEntry - shortTargetTwo) * exitShortSizeTwo, 2)
    Label(window, text=shortProfitOne).grid(row=5, column=2)
    Label(window, text=shortProfitTwo).grid(row=6, column=2)

    totalShortProfit = round(shortProfitOne + shortProfitTwo, 2)
    Label(window, text=totalShortProfit).grid(row=8, column=2)

window = Tk()
window.geometry("350x250")
window.title("Range Break V2")

Label(window, text="Enter Risk").grid(row=0, column=0)
RISK = DoubleVar()
riskInput = Entry(window, textvariable=RISK).grid(row=0, column=1)

Label(window, text="Enter Range High").grid(row=1, column=0)
rangeHigh = DoubleVar()
rangeHighInput = Entry(window, textvariable=rangeHigh).grid(row=1, column=1)

Label(window, text="Enter Range Low").grid(row=2, column=0)
rangeLow = DoubleVar()
rangeLowInput = Entry(window, textvariable=rangeLow).grid(row=2, column=1)

Label(window, text="# of Shares").grid(row=4, column=0)
Label(window, text="Targets").grid(row=4, column=1)
Label(window, text="Potential Profit").grid(row=4, column =2)
Label(window, text="Total Shares").grid(row=7, column=0)
Label(window, text="Position Value").grid(row=7, column=1)
Label(window, text="Total Profit").grid(row=7, column=2)
Label(window, text="Entry Price").grid(row=9, column=0)
Label(window, text="Stop Price").grid(row=9, column=1)
Label(window, text="Total Risk").grid(row=9, column=2)

longButton = Button(window, text="Long", command=longCalc).grid(row=3, column=0)
shortButton = Button(window, text="Short", command=shortCalc).grid(row=3, column=1)
quitButton = Button(window, text="Quit", command=window.quit).grid(row=3, column=2)

window.mainloop()