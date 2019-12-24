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

def shortCalc(entries):
    # total share size calc
    rangeHigh = float(entries['Range High'].get())
    rangeLow = float(entries['Range Low'].get())
    rangeWidth = rangeHigh - rangeLow
    shortShareSize = round((float(entries['Risk'].get()))/rangeWidth, -1)
    print("Total Short Share Size = ", shortShareSize)
    entries['Total Shares'].delete(0, tk.END)
    entries['Total Shares'].insert(0, shortShareSize)

    #entry price calc
    shortEntry = rangeLow - 0.01
    print("Short Entry Price = ", shortEntry)
    entries['Entry Price'].delete(0, tk.END)
    entries['Entry Price'].insert(0, shortEntry)

    #position value calc
    positionValue = round(shortEntry * shortShareSize, 2)
    print("Position Value = ", positionValue)
    entries['Position Value'].delete(0, tk.END)
    entries['Position Value'].insert(0, positionValue)

    totalShortRisk = round(shortShareSize*(rangeHigh-shortEntry), 2)
    print("Total Risk Short = ", totalShortRisk)
    entries['Total Risk'].delete(0, tk.END)
    entries['Total Risk'].insert(0, totalShortRisk)

    shortStop = rangeHigh
    print("Short Stop Price = ", shortStop)
    entries['Stop Price'].delete(0, tk.END)
    entries['Stop Price'].insert(0, shortStop)

    shortTargetOne = shortEntry-rangeWidth
    shortTargetTwo = shortTargetOne-rangeWidth
    print("Short Target One = ", shortTargetOne)
    print("Short Target Two = ", shortTargetTwo)
    entries['T1'].delete(0, tk.END)
    entries['T2'].delete(0, tk.END)
    entries['T1'].insert(0, shortTargetOne)
    entries['T2'].insert(0, shortTargetTwo)


    exitShortSizeOne = round(shortShareSize/2, -1)
    print("First Share Exit Size = ", exitShortSizeOne)
    exitShortSizeTwo = shortShareSize-exitShortSizeOne
    print("Second Share Exit Size = ", exitShortSizeTwo)
    entries['S1'].delete(0, tk.END)
    entries['S2'].delete(0, tk.END)
    entries['S1'].insert(0, exitShortSizeOne)
    entries['S2'].insert(0, exitShortSizeTwo)

    shortProfitOne = round((shortEntry - shortTargetOne) * exitShortSizeOne, 2)
    shortProfitTwo = round((shortEntry - shortTargetTwo) * exitShortSizeTwo, 2)
    print("Profit on first Target = ", shortProfitOne)
    print("Profit on second Target = ", shortProfitTwo)
    entries['P1'].delete(0, tk.END)
    entries['P2'].delete(0, tk.END)
    entries['P1'].insert(0, shortProfitOne)
    entries['P2'].insert(0, shortProfitTwo)

    totalShortProfit = round(shortProfitOne + shortProfitTwo, 2)
    print("Total Short Profit = ", totalShortProfit)
    entries['Total Profit'].delete(0, tk.END)
    entries['Total Profit'].insert(0, totalShortProfit)


    shortRisk2Reward = round(totalShortProfit/totalShortRisk, 2)
    print("Short R2R = ", shortRisk2Reward)
    entries['R2R'].delete(0, tk.END)
    entries['R2R'].insert(0, shortRisk2Reward)



def longCalc(entries):
    # total share size calc
    rangeHigh = float(entries['Range High'].get())
    rangeLow = float(entries['Range Low'].get())
    rangeWidth = rangeHigh - rangeLow
    longShareSize = round((float(entries['Risk'].get())) / rangeWidth, -1)
    print("Total Long Share Size = ", longShareSize)
    entries['Total Shares'].delete(0, tk.END)
    entries['Total Shares'].insert(0, longShareSize)

    # entry price calc
    longEntry = rangeHigh + 0.01
    print("Long Entry Price = ", longEntry)
    entries['Entry Price'].delete(0, tk.END)
    entries['Entry Price'].insert(0, longEntry)

    # position value calc
    positionValue = round(longEntry * longShareSize, 2)
    print("Position Value = ", positionValue)
    entries['Position Value'].delete(0, tk.END)
    entries['Position Value'].insert(0, positionValue)

    totalLongRisk = round(longShareSize * (longEntry - rangeLow), 2)
    print("Total Risk Long = ", totalLongRisk)
    entries['Total Risk'].delete(0, tk.END)
    entries['Total Risk'].insert(0, totalLongRisk)

    longStop = rangeLow
    print("Long Stop Price = ", longStop)
    entries['Stop Price'].delete(0, tk.END)
    entries['Stop Price'].insert(0, longStop)

    longTargetOne = longEntry + rangeWidth
    longTargetTwo = longTargetOne + rangeWidth
    print("Long Target One = ", longTargetOne)
    print("Long Target Two = ", longTargetTwo)
    entries['T1'].delete(0, tk.END)
    entries['T2'].delete(0, tk.END)
    entries['T1'].insert(0, longTargetOne)
    entries['T2'].insert(0, longTargetTwo)

    exitLongSizeOne = round(longShareSize / 2, -1)
    print("First Share Exit Size = ", exitLongSizeOne)
    exitLongSizeTwo = longShareSize - exitLongSizeOne
    print("Second Share Exit Size = ", exitLongSizeTwo)
    entries['S1'].delete(0, tk.END)
    entries['S2'].delete(0, tk.END)
    entries['S1'].insert(0, exitLongSizeOne)
    entries['S2'].insert(0, exitLongSizeTwo)

    longProfitOne = round((longTargetOne - longEntry) * exitLongSizeOne, 2)
    longProfitTwo = round((longTargetTwo - longEntry) * exitLongSizeTwo, 2)
    print("Profit on first Target = ", longProfitOne)
    print("Profit on second Target = ", longProfitTwo)
    entries['P1'].delete(0, tk.END)
    entries['P2'].delete(0, tk.END)
    entries['P1'].insert(0, longProfitOne)
    entries['P2'].insert(0, longProfitTwo)

    totalLongProfit = round(longProfitOne + longProfitTwo, 2)
    print("Total Long Profit = ", totalLongProfit)
    entries['Total Profit'].delete(0, tk.END)
    entries['Total Profit'].insert(0, totalLongProfit)

    longRisk2Reward = round(totalLongProfit / totalLongRisk, 2)
    print("Long R2R = ", longRisk2Reward)
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