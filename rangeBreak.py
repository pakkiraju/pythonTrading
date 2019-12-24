###############################################################################
### Creator         : Pradhamesh Akkiraju                                   ###
### Date            : December 23/2019                                      ###
### Project Name    : rangeBreak                                            ###
### Description     : This is a target, share, loss calculator              ###
###                   based on a range break that is specified by the user  ###
###############################################################################

# Imports
import tkinter as tk

# The fields to display
fields = ('Risk', 'Range High', 'Range Low', 'Entry Price', 'Stop Price', 'T1', 'S1', 'P1', 'T2', 'S2', 'P2', 'Total Profit', 'Total Shares', 'Total Risk', 'R2R', 'Position Value')

# Below contains the formulas for the short side.
def shortCalc(entries):

    # Total Shares calculator
    rangeHigh = float(entries['Range High'].get())
    rangeLow = float(entries['Range Low'].get())
    rangeWidth = rangeHigh - rangeLow
    shortShareSize = round((float(entries['Risk'].get()))/rangeWidth, -1)
    print("Total Short Share Size = ", shortShareSize)
    # Outputs the Total Share Size for the Short Side
    entries['Total Shares'].delete(0, tk.END)
    entries['Total Shares'].insert(0, shortShareSize)

    # Entry Price Calculator
    shortEntry = rangeLow - 0.01
    print("Short Entry Price = ", shortEntry)
    # Outputs the Entry Price for the Short Side
    entries['Entry Price'].delete(0, tk.END)
    entries['Entry Price'].insert(0, shortEntry)

    # Position Value Calculator
    positionValue = round(shortEntry * shortShareSize, 2)
    print("Position Value = ", positionValue)
    # Outputs the Position Value for the Short Side
    entries['Position Value'].delete(0, tk.END)
    entries['Position Value'].insert(0, positionValue)

    # Total Risk Calculator
    totalShortRisk = round(shortShareSize*(rangeHigh-shortEntry), 2)
    print("Total Risk Short = ", totalShortRisk)
    # Outputs the Risk for Short Side
    entries['Total Risk'].delete(0, tk.END)
    entries['Total Risk'].insert(0, totalShortRisk)

    # Stop loss deceleration
    shortStop = rangeHigh
    print("Short Stop Price = ", shortStop)
    # Outputs the Stop Loss for Short Side
    entries['Stop Price'].delete(0, tk.END)
    entries['Stop Price'].insert(0, shortStop)

    # Target One and Two Calculator
    shortTargetOne = shortEntry-rangeWidth
    shortTargetTwo = shortTargetOne-rangeWidth
    print("Short Target One = ", shortTargetOne)
    print("Short Target Two = ", shortTargetTwo)
    # Outputs Target One and Two for Short Side
    entries['T1'].delete(0, tk.END)
    entries['T2'].delete(0, tk.END)
    entries['T1'].insert(0, shortTargetOne)
    entries['T2'].insert(0, shortTargetTwo)

    # Exit Size Calculator
    exitShortSizeOne = round(shortShareSize/2, -1)
    print("First Share Exit Size = ", exitShortSizeOne)
    exitShortSizeTwo = shortShareSize-exitShortSizeOne
    print("Second Share Exit Size = ", exitShortSizeTwo)
    # Outputs the Exit Share Sizes for the Short Side
    entries['S1'].delete(0, tk.END)
    entries['S2'].delete(0, tk.END)
    entries['S1'].insert(0, exitShortSizeOne)
    entries['S2'].insert(0, exitShortSizeTwo)

    # Profit One and Two Calculator
    shortProfitOne = round((shortEntry - shortTargetOne) * exitShortSizeOne, 2)
    shortProfitTwo = round((shortEntry - shortTargetTwo) * exitShortSizeTwo, 2)
    print("Profit on first Target = ", shortProfitOne)
    print("Profit on second Target = ", shortProfitTwo)
    # Outputs Profit One and Two for the Short Side
    entries['P1'].delete(0, tk.END)
    entries['P2'].delete(0, tk.END)
    entries['P1'].insert(0, shortProfitOne)
    entries['P2'].insert(0, shortProfitTwo)

    # Total Profit Calculator
    totalShortProfit = round(shortProfitOne + shortProfitTwo, 2)
    print("Total Short Profit = ", totalShortProfit)
    # Outputs Total Profit for the Short Side
    entries['Total Profit'].delete(0, tk.END)
    entries['Total Profit'].insert(0, totalShortProfit)

    # Risk 2 Reward Calculator
    shortRisk2Reward = round(totalShortProfit/totalShortRisk, 2)
    print("Short R2R = ", shortRisk2Reward)
    # Outputs the R2R for the Short Side
    entries['R2R'].delete(0, tk.END)
    entries['R2R'].insert(0, shortRisk2Reward)



def longCalc(entries):

    # Total Shares calculator
    rangeHigh = float(entries['Range High'].get())
    rangeLow = float(entries['Range Low'].get())
    rangeWidth = rangeHigh - rangeLow
    longShareSize = round((float(entries['Risk'].get())) / rangeWidth, -1)
    print("Total Long Share Size = ", longShareSize)
    # Outputs the Total Share Size for the Long Side
    entries['Total Shares'].delete(0, tk.END)
    entries['Total Shares'].insert(0, longShareSize)

    # Entry Price Calculator
    longEntry = rangeHigh + 0.01
    print("Long Entry Price = ", longEntry)
    # Outputs the Entry Price for the Long Side
    entries['Entry Price'].delete(0, tk.END)
    entries['Entry Price'].insert(0, longEntry)

    # Position Value Calculator
    positionValue = round(longEntry * longShareSize, 2)
    print("Position Value = ", positionValue)
    # Outputs the Position Value for the Long Side
    entries['Position Value'].delete(0, tk.END)
    entries['Position Value'].insert(0, positionValue)

    # Total Risk Calculator
    totalLongRisk = round(longShareSize * (longEntry - rangeLow), 2)
    print("Total Risk Long = ", totalLongRisk)
    # Outputs the Risk for Long Side
    entries['Total Risk'].delete(0, tk.END)
    entries['Total Risk'].insert(0, totalLongRisk)

    # Stop loss deceleration
    longStop = rangeLow
    print("Long Stop Price = ", longStop)
    # Outputs the Stop Loss for Long Side
    entries['Stop Price'].delete(0, tk.END)
    entries['Stop Price'].insert(0, longStop)

    # Target One and Two Calculator
    longTargetOne = longEntry + rangeWidth
    longTargetTwo = longTargetOne + rangeWidth
    print("Long Target One = ", longTargetOne)
    print("Long Target Two = ", longTargetTwo)
    # Outputs Target One and Two for Long Side
    entries['T1'].delete(0, tk.END)
    entries['T2'].delete(0, tk.END)
    entries['T1'].insert(0, longTargetOne)
    entries['T2'].insert(0, longTargetTwo)

    # Exit Size Calculator
    exitLongSizeOne = round(longShareSize / 2, -1)
    print("First Share Exit Size = ", exitLongSizeOne)
    exitLongSizeTwo = longShareSize - exitLongSizeOne
    print("Second Share Exit Size = ", exitLongSizeTwo)
    # Outputs the Exit Share Sizes for the Long Side
    entries['S1'].delete(0, tk.END)
    entries['S2'].delete(0, tk.END)
    entries['S1'].insert(0, exitLongSizeOne)
    entries['S2'].insert(0, exitLongSizeTwo)

    # Profit One and Two Calculator
    longProfitOne = round((longTargetOne - longEntry) * exitLongSizeOne, 2)
    longProfitTwo = round((longTargetTwo - longEntry) * exitLongSizeTwo, 2)
    print("Profit on first Target = ", longProfitOne)
    print("Profit on second Target = ", longProfitTwo)
    # Outputs Profit One and Two for the Long Side
    entries['P1'].delete(0, tk.END)
    entries['P2'].delete(0, tk.END)
    entries['P1'].insert(0, longProfitOne)
    entries['P2'].insert(0, longProfitTwo)

    # Total Profit Calculator
    totalLongProfit = round(longProfitOne + longProfitTwo, 2)
    print("Total Long Profit = ", totalLongProfit)
    # Outputs Total Profit for the Long Side
    entries['Total Profit'].delete(0, tk.END)
    entries['Total Profit'].insert(0, totalLongProfit)

    # Risk 2 Reward Calculator
    longRisk2Reward = round(totalLongProfit / totalLongRisk, 2)
    print("Long R2R = ", longRisk2Reward)
    # Outputs the R2R for the Long Side
    entries['R2R'].delete(0, tk.END)
    entries['R2R'].insert(0, longRisk2Reward)

def makeform(root, fields):
    entries = {}
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP,
                 fill=tk.X,
                 padx=5,
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT,
                 expand=tk.NO,
                 fill=tk.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("300x600")
    root.title("Range Break Calculator")
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Long', command=(lambda e=ents: longCalc(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Short', command=(lambda e=ents: shortCalc(e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()