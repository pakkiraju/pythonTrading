import tkinter as tk

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
    positionValue = shortEntry * shortShareSize
    print("Position Value = ", positionValue)
    entries['Position Value'].delete(0, tk.END)
    entries['Position Value'].insert(0, positionValue)

    totalShortRisk = shortShareSize*(rangeHigh-shortEntry)
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

    shortProfitOne = (shortEntry - shortTargetOne) * exitShortSizeOne
    shortProfitTwo = (shortEntry - shortTargetTwo) * exitShortSizeTwo
    print("Profit on first Target = ", shortProfitOne)
    print("Profit on second Target = ", shortProfitTwo)
    entries['P1'].delete(0, tk.END)
    entries['P2'].delete(0, tk.END)
    entries['P1'].insert(0, shortProfitOne)
    entries['P2'].insert(0, shortProfitTwo)

    totalShortProfit = shortProfitOne + shortProfitTwo
    print("Total Short Profit = ", totalShortProfit)
    entries['Total Profit'].delete(0, tk.END)
    entries['Total Profit'].insert(0, totalShortProfit)


    shortRisk2Reward = totalShortProfit/totalShortRisk
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
    positionValue = longEntry * longShareSize
    print("Position Value = ", positionValue)
    entries['Position Value'].delete(0, tk.END)
    entries['Position Value'].insert(0, positionValue)

    totalLongRisk = longShareSize * (longEntry - rangeLow)
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

    longProfitOne = (longTargetOne - longEntry) * exitLongSizeOne
    longProfitTwo = (longTargetTwo - longEntry) * exitLongSizeTwo
    print("Profit on first Target = ", longProfitOne)
    print("Profit on second Target = ", longProfitTwo)
    entries['P1'].delete(0, tk.END)
    entries['P2'].delete(0, tk.END)
    entries['P1'].insert(0, longProfitOne)
    entries['P2'].insert(0, longProfitTwo)

    totalLongProfit = longProfitOne + longProfitTwo
    print("Total Long Profit = ", totalLongProfit)
    entries['Total Profit'].delete(0, tk.END)
    entries['Total Profit'].insert(0, totalLongProfit)

    longRisk2Reward = totalLongProfit / totalLongRisk
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
                 expand=tk.YES,
                 fill=tk.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("500x600")
    root.title("Range Break Calculator by Prad")
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Long',
           command=(lambda e=ents: longCalc(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Short',
           command=(lambda e=ents: shortCalc(e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()