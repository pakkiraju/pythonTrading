###############################################################################
### Creator         : Pradhamesh Akkiraju                                   ###
### Date Created    : December 23/2019                                      ###
### Project Name    : rangeBreakV2                                          ###
### Description     : This is a target, share, loss calculator              ###
###                   based on a range break that is specified by the user  ###
### Version Code    : 2.0.0                                                 ###
### Last Updated    : December 24/2019                                      ###
###############################################################################

# Imports
from tkinter import *
import os

# Create a function for the Long side that contains all the formulas
def longCalc():
    # Setting 'root' as the pop-up window name which happens within the 'window' which is the main GUI
    root = Toplevel(window)
    # Setting the pop-up window title
    tickerText = ticker.get()
    root.title(tickerText)
    root.geometry("300x150")
    # Setting Pop-up window Icon
    path = os.getcwd()
    root.iconbitmap(path+"\ICONS\Visualpharm-Must-Have-Stock-Index-Up.ico")

    # Setting Text Labels to form tables (overall formatting of the output)
    Label(root, text="# of Shares").grid(row=4, column=0)
    Label(root, text="Targets").grid(row=4, column=1)
    Label(root, text="Potential Profit").grid(row=4, column=2)
    Label(root, text="Total Shares").grid(row=7, column=0)
    Label(root, text="Position Value").grid(row=7, column=1)
    Label(root, text="Total Profit").grid(row=7, column=2)
    Label(root, text="Entry Price").grid(row=9, column=0)
    Label(root, text="Stop Price").grid(row=9, column=1)
    Label(root, text="Total Risk").grid(row=9, column=2)

    # Declare Variables to the responding Input Boxes
    longRangeHigh = rangeHigh.get()
    longRangeLow = rangeLow.get()
    longRisk = RISK.get()
    rangeWidth = longRangeHigh - longRangeLow

    # Share Size Calculation
    longShareSize = round(longRisk / rangeWidth, -1)
    Label(root, text=longShareSize).grid(row=8, column=0)

    # Entry Price Calculation
    longEntry = round(longRangeHigh + 0.01, 2)
    Label(root, text=longEntry).grid(row=10, column=0)

    # Position Value Calculation
    positionValue = round(longEntry * longShareSize, 2)
    Label(root, text=positionValue).grid(row=8, column=1)

    # Risk Calculation
    totalLongRisk = round(longShareSize * (longEntry - longRangeLow), 2)
    Label(root, text=totalLongRisk).grid(row=10, column=2)

    # Stop Calculation
    longStop = longRangeLow-0.01
    Label(root, text=longStop).grid(row=10, column=1)

    # Target One and Two Calculation
    longTargetOne = round(longEntry + rangeWidth, 2)
    longTargetTwo = round(longTargetOne + rangeWidth, 2)
    Label(root, text=longTargetOne).grid(row=5, column=1)
    Label(root, text=longTargetTwo).grid(row=6, column=1)

    if longShareSize == 10:
        exitLongSizeOne = longShareSize
        Label(root, text=exitLongSizeOne).grid(row=5, column=0)
    else:
        # Exit Sizes One and Two Calculation
        exitLongSizeOne = round(longShareSize / 2, -1)
        Label(root, text=exitLongSizeOne).grid(row=5, column=0)

    exitLongSizeTwo = longShareSize - exitLongSizeOne
    Label(root, text=exitLongSizeTwo).grid(row=6, column=0)

    # Profit One and Two Calculation
    longProfitOne = round((longTargetOne - longEntry) * exitLongSizeOne, 2)
    longProfitTwo = round((longTargetTwo - longEntry) * exitLongSizeTwo, 2)
    Label(root, text=longProfitOne).grid(row=5, column=2)
    Label(root, text=longProfitTwo).grid(row=6, column=2)

    # Total Profit Calculation
    totalLongProfit = round(longProfitOne + longProfitTwo, 2)
    Label(root, text=totalLongProfit).grid(row=8, column=2)

# Create a function for the Short side that contains all the formulas
def shortCalc():
    # Setting 'root' as the pop-up window name which happens within the 'window' which is the main GUI
    root = Toplevel(window)
    # Setting the pop-up window title
    tickerText = ticker.get()
    root.title(tickerText)
    root.geometry("300x150")
    # Setting Pop-up window Icon
    path = os.getcwd()
    root.iconbitmap(path+"\ICONS\Visualpharm-Must-Have-Stock-Index-Down.ico")

    # Setting Text Labels to form tables (overall formatting of the output)
    Label(root, text="# of Shares").grid(row=4, column=0)
    Label(root, text="Targets").grid(row=4, column=1)
    Label(root, text="Potential Profit").grid(row=4, column=2)
    Label(root, text="Total Shares").grid(row=7, column=0)
    Label(root, text="Position Value").grid(row=7, column=1)
    Label(root, text="Total Profit").grid(row=7, column=2)
    Label(root, text="Entry Price").grid(row=9, column=0)
    Label(root, text="Stop Price").grid(row=9, column=1)
    Label(root, text="Total Risk").grid(row=9, column=2)

    # Declare Variables to the responding Input Boxes
    shortRangeHigh = rangeHigh.get()
    shortRangeLow = rangeLow.get()
    shortRisk = RISK.get()
    rangeWidth = shortRangeHigh - shortRangeLow

    # Share Size Calculation
    shortShareSize = round(shortRisk / rangeWidth, -1)
    Label(root, text=shortShareSize).grid(row=8, column=0)

    # Entry Price Calculation
    shortEntry = round(shortRangeLow - 0.01, 2)
    Label(root, text=shortEntry).grid(row=10, column=0)

    # Position Value Calculation
    positionValue = round(shortEntry * shortShareSize, 2)
    Label(root, text=positionValue).grid(row=8, column=1)

    # Risk Calculation
    totalShortRisk = round(shortShareSize * (shortRangeHigh - shortEntry), 2)
    Label(root, text=totalShortRisk).grid(row=10, column=2)

    # Stop Calculation
    shortStop = shortRangeHigh+0.01
    Label(root, text=shortStop).grid(row=10, column=1)

    # Target One and Two Calculation
    shortTargetOne = round(shortEntry - rangeWidth, 2)
    shortTargetTwo = round(shortTargetOne - rangeWidth, 2)
    Label(root, text=shortTargetOne).grid(row=5, column=1)
    Label(root, text=shortTargetTwo).grid(row=6, column=1)

    if shortShareSize == 10:
        exitShortSizeOne = shortShareSize
        Label(root, text=exitShortSizeOne).grid(row=5, column=0)
    else:
        # Exit Sizes One and Two Calculation
        exitShortSizeOne = round(shortShareSize / 2, -1)
        Label(root, text=exitShortSizeOne).grid(row=5, column=0)

    exitShortSizeTwo = shortShareSize - exitShortSizeOne
    Label(root, text=exitShortSizeTwo).grid(row=6, column=0)

    # Profit One and Two Calculation
    shortProfitOne = round((shortEntry - shortTargetOne) * exitShortSizeOne, 2)
    shortProfitTwo = round((shortEntry - shortTargetTwo) * exitShortSizeTwo, 2)
    Label(root, text=shortProfitOne).grid(row=5, column=2)
    Label(root, text=shortProfitTwo).grid(row=6, column=2)

    # Total Profit Calculation
    totalShortProfit = round(shortProfitOne + shortProfitTwo, 2)
    Label(root, text=totalShortProfit).grid(row=8, column=2)

# Creates the GUI Window
window = Tk()
# Declares the window box size
window.geometry("200x120")
# Set GUI Title
window.title("Range Break V.2.0.0")
# Setting Window Icon
path = os.getcwd()
window.iconbitmap(path+"\ICONS\Iynque-Ios7-Style-Stocks.ico")

# Setting Labels and Giving then Input Boxes to get data from user
Label(window, text="Enter Risk").grid(row=0, column=0)
RISK = DoubleVar()
riskInput = Entry(window, textvariable=RISK).grid(row=0, column=1)

Label(window, text="Enter Range High").grid(row=1, column=0)
rangeHigh = DoubleVar()
rangeHighInput = Entry(window, textvariable=rangeHigh).grid(row=1, column=1)

Label(window, text="Enter Range Low").grid(row=2, column=0)
rangeLow = DoubleVar()
rangeLowInput = Entry(window, textvariable=rangeLow).grid(row=2, column=1)

Label(window, text="Enter Ticker").grid(row=3, column=0)
ticker = StringVar()
tickerInput = Entry(window, textvariable=ticker).grid(row=3, column=1)

# Long / Short / Quit buttons
longButton = Button(window, text="Long", command=longCalc).grid(row=4, column=0)
shortButton = Button(window, text="Short", command=shortCalc).grid(row=4, column=1)

# Runs the GUI loop
window.mainloop()