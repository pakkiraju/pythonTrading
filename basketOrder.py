###############################################################################
### Creator         : Pradhamesh Akkiraju                                   ###
### Date            : December 23/2019                                      ###
### Project Name    : basketOrder.py                                        ###
### Description     : This program is used to help calculate the            ###
###                     appropriate basket size for EU/TSX/NYSE MOC Trades  ###
###############################################################################

# Imports
import requests
from tkinter import *

from bs4 import BeautifulSoup


def calculate():
    bpPerStock = round(buyingPower.get() / numberOfStocks.get(), 2)
    Label(window, text=bpPerStock).grid(row=2, column=1)

    tickerOneText = tickerOne.get()
    tickerOneURL = 'https://ca.finance.yahoo.com/quote/%s' % tickerOneText
    requestOne = requests.get(tickerOneURL)
    soup = BeautifulSoup(requestOne.content, 'html5lib')
    tickerOnePrice = soup.find('span')
    print(tickerOnePrice)

window = Tk()
window.geometry("500x500")
window.title("Basket Order Calculator")

Label(window, text="Enter Buying Power").grid(row=0, column=0)
buyingPower = DoubleVar()
buyingPower_inputBox = Entry(window, textvariable=buyingPower).grid(row=0, column=1)

Label(window, text="Enter # of Stocks").grid(row=1, column=0)
numberOfStocks = DoubleVar()
numberOfStocks_inputBox = Entry(window, textvariable=numberOfStocks).grid(row=1, column=1)

Label(window, text="BP Per Stock =").grid(row=2, column=0)

Label(window, text="Ticker(s)").grid(row=3, column=0)
Label(window, text="Stock Price").grid(row=3, column=1)
Label(window, text="Share Size").grid(row=3, column=2)
Label(window, text="BP Invested").grid(row=3, column=3)

tickerOne = StringVar()
tickerTwo = StringVar()
tickerThree = StringVar()
tickerFour = StringVar()
tickerFive = StringVar()
tickerSix = StringVar()
tickerSeven = StringVar()
tickerEight = StringVar()
tickerNine = StringVar()
tickerTen = StringVar()
tickerOne_IB = Entry(window, textvariable=tickerOne).grid(row=4, column=0)
tickerTwo_IB = Entry(window, textvariable=tickerTwo).grid(row=5, column=0)
tickerThree_IB = Entry(window, textvariable=tickerThree).grid(row=6, column=0)
tickerFour_IB = Entry(window, textvariable=tickerFour).grid(row=7, column=0)
tickerFive_IB = Entry(window, textvariable=tickerFive).grid(row=8, column=0)
tickerSix_IB = Entry(window, textvariable=tickerSix).grid(row=9, column=0)
tickerSeven_IB = Entry(window, textvariable=tickerSeven).grid(row=10, column=0)
tickerEight_IB = Entry(window, textvariable=tickerEight).grid(row=11, column=0)
tickerNine_IB = Entry(window, textvariable=tickerNine).grid(row=12, column=0)
tickerTen_IB = Entry(window, textvariable=tickerTen).grid(row=13, column=0)

calculateButton = Button(window, text="Calculate", command=calculate).grid(row=14, column=0)

window.mainloop()